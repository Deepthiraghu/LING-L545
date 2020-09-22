#!/usr/bin/env python3
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
output = open('punkt.txt', 'w', encoding='utf-8')
text = ''
with open('wiki.txt', 'r', encoding='utf-8') as f:
    for l in f:
        if l == '\n':
            output.write('\n'.join(sent_tokenize(text))+'\n')
            text = ''
            continue
        text += l
output.close()
