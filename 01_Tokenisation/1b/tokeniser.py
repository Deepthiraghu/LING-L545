import sys
import re

input_text = sys.stdin.readline()

sentence_count = 1

while input_text != '':
    print('sentence ID =', sentence_count)
    sentence_count += 1
    input_text = input_text.strip()

    # preprocess the text to add a space before or after certain punctuation characters
    singlequote = input_text.replace("'","' ")
    doublequote  = singlequote.replace('"',' " ')
    comma = doublequote.replace(',', ' , ')
    fullstop = comma.replace('.', ' .')
    paranthesis_open = fullstop.replace('(', ' ( ')
    paranthesis_close = paranthesis_open.replace(')', ' ) ')
    asterisk = re.sub('  *', ' ', paranthesis_close)

    print('sentence =', asterisk)
    sentence = asterisk.split(' ')
    word_count = 1

    for i in sentence:
        if i != '.':
            print (word_count, i, '  _', '   _', '   _', '   _', '   _', '   _', '   _', '   _')
            word_count += 1
        else:
            print (word_count, '.', '  _', '   _', '   _', '   _', '   _', '   _', '   _', '   _')

    input_text = sys.stdin.readline()
