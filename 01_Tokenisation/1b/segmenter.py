import sys

input_text = sys.stdin.readline()

# replace every full stop '.' followed by a space ' ' with a full stop and a newline character '\n'
while input_text != '':
    if input_text.strip() == '':
        input_text = sys.stdin.readline()
        continue
    
    text_end = input_text.strip().replace('. ', '.\n').strip()

    if text_end != '':
        print(text_end.strip())
    input_text = sys.stdin.readline()
