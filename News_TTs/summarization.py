#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from transformers import BartTokenizer, BartForConditionalGeneration

# Load the BART model and tokenizer for summarization
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
summarization_model = BartForConditionalGeneration.from_pretrained(model_name)

def summarize_text(text, max_length=1024):
    if not text or not isinstance(text, str):
        return ""
    
    input_text = "summarize: " + text
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=1024, truncation=True)
    
    summary_ids = summarization_model.generate(
        inputs, 
        max_length=max_length, 
        min_length=200,  # Increase min_length for longer summaries
        length_penalty=1.5,  # Reduce penalty for more balanced output
        num_beams=6,  # Increase num_beams for better quality summary
        repetition_penalty=1.2,  # Reduce repetition
        early_stopping=True
    )
    
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


