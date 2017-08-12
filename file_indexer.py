import re
from collections import defaultdict, Counter

pattern = re.compile('[^a-zA-Z0-9]+')

def blobToWords(blobStr: str)-> list:
    words = pattern.split(blobStr)
    for i in (0, -1):
        if not words[i]:
            words.pop(i)
    return words

def topTenWordCounts(words: list)-> list:
    c = defaultdict(int)
    for word in words:
        c[word.lower()] += 1
        
    return sorted(c.items(), key=lambda x: x[1],
                  reverse=True)[:10]
