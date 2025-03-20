#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import yake
from collections import Counter

def extract_topics(texts):
    kw_extractor = yake.KeywordExtractor()
    keywords = []
    for text in texts:
        extracted_keywords = kw_extractor.extract_keywords(text)
        keywords.extend([kw[0] for kw in extracted_keywords[:3]])  # Top 3 keywords per text
    # Get the most common keywords
    common_keywords = Counter(keywords).most_common(5)  # Top 5 most common keywords
    return [kw[0] for kw in common_keywords]

