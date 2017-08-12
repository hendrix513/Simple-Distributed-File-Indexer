import re
from collections import defaultdict, Counter

pattern = re.compile('[^a-zA-Z0-9]+')

def blobToWords(blobStr)
    words = pattern.split(blobStr)
    for i in (0, -1):
        if not words[i]:
            words.pop(i)
    return words

def topTenWordCounts(words)
    c = defaultdict(int)
    for word in words:
        c[word.lower()] += 1
        
    return sorted(c.items(), key=lambda x: x[1],
                  reverse=True)[:10]

def main():
    print 'Top Ten Word Counts: {0}'.format(wordCounter(docs))
    
if __name__ == '__main__':
    main()
