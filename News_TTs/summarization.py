import os
import requests

# Hugging Face Inference API endpoint for BART summarization
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {os.getenv('HUGGING_FACE_TOKEN')}"}  

def summarize_text(text, max_length=1024):
    if not text or not isinstance(text, str):
        return ""
    
    # Prepare the payload for the API request
    payload = {
        "inputs": text,
        "parameters": {
            "max_length": max_length,
            "min_length": 200,  
            "length_penalty": 1.5,  
            "num_beams": 6,  
            "repetition_penalty": 1.2,  
            "early_stopping": True
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  
        result = response.json()
        return result[0]['summary_text']
    except Exception as e:
        print(f"Error during summarization: {e}")
        return ""
