import argparse
import os, sys
import re
from collections import defaultdict
from multiprocessing import Pool

pattern = re.compile('[^a-zA-Z0-9]+')

def read_docs(docs):
    for doc in docs:
        with open(doc, 'r') as f:
            while True:
                data = f.readlines(100)
                if not data:
                    break
                yield ''.join(data)

def blobToWordsGenerator(blobStr):
    '''
    converts blobStr into a generator of strings, split by any character that
    matches 'pattern'. This function is unused by CLI but I thought it would
    be cool to use this function instead of blobToWords, given more time

    args:
        blobStr: str

    returns:
        generator of strings
    '''
    cPattern = re.compile('[^a-zA-Z0-9]+')
    word = ''
    for c in blobStr:
        if cPattern.match(c):
            word = '{0}{1}'.format(word, c)
        else:
            if word:
                yield word
                word = ''
    if word:
        yield word

def blobToWords(blobStr):
    '''
    converts blobStr into a list of strings, split by any character that matches
    'pattern'
    
    args:
        blobStr: str
        
    returns:
        list of strings
    '''
    words = pattern.split(blobStr)
    if not words:
        return words

    for i in (0, -1):
        if not words[i]:
            words.pop(i)
            if not words:
                return words
    return words

def topTenWordCounts(words):
    '''
    args:
        words: iterable of strings
    returns:
        list of tuples of length 10 or less,
         each of length 2. 
         First item of each tuple is a string, second is the number of times
         that string, ignoring capitalization, occurs in 'words'.
         list includes only the top 10 most frequent
         words if the length of words is 10 or greater, or all words
         otherwise
    '''
    c = defaultdict(int)
    for word in words:
        c[word.lower()] += 1

    return sorted(c.items(), key=lambda x: x[1],
                  reverse=True)[:10]

def iterateWordsList(wordsList):
    '''
    generator function for list of 'words' lists, the result of a pool of
    processes executing 'blobToStr'  
    '''
    for words in wordsList:
        for word in words:
            yield word

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs='+', help="file to index")
    args = parser.parse_args()
    docs = [os.path.abspath(doc) for doc in args.file]

    pool = Pool(processes=8)
    wordsList = pool.map(blobToWords, read_docs(docs))
    pool.close()
    pool.join()

    print('Top Ten Word Counts:\n {0}'.format(topTenWordCounts(
        iterateWordsList(wordsList))))

if __name__ == '__main__':
    main()
    sys.exit(0)
