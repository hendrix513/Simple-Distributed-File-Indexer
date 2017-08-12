import re
pattern = re.compile('[^a-zA-Z0-9]+')

def blobToWords(blobStr):
    words = pattern.split(blobStr)
    for i in (0, -1):
        if not l[i]:
            l.pop(i)
    return l
