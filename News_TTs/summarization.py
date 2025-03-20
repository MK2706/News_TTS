#!/usr/bin/env python
# coding: utf-8

import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer HB_API_HERE"}

def summarize_text_using_api(text, max_length=1024, min_length=200):
    if not text or not isinstance(text, str):
        return ""

    payload = {
        "inputs": text,
        "parameters": {
            "max_length": max_length,
            "min_length": min_length,
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

def summarize_text(text, max_length=1024, min_length=200):
    return summarize_text_using_api(text, max_length, min_length)
