import sys 

chars = 0 # varable to count characters
tokens = 0 # varable to count tokens
vowels = 0 # varable to count vowels
consonants = 0 # varable to count consonants

input_text = sys.stdin.read() # read from command lines

for character in input_text:
    lines = len(input_text.splitlines()) # read input text line by line

    # count characters
    if character.isalpha(): 
        chars +=1 

    # count tokens by splitting using spaces
    tokens = len(input_text.split()) 

    # count vowels
    if character.isalpha() and character in 'aeiuoAEIUO': 
        vowels += 1

    # count consonants
    elif character.isalpha() and character not in 'aeiuoAIUOE':
        consonants +=1

# print results
print( "Number of lines: ", lines , "\n Number of tokens: ", tokens, "\n Number of characters: ", chars, "\n Number of vowels: ", vowels, "\n Number of consonants: ", consonants, "\n Average number of syllables per word", chars/vowels) 

# The average number of syllables may be wrong in cases like the word "day", where 'y' sounds like a vowel, but is not recognized in the above calculation.
# In case on "day", the actual number of syllables is 1, but my program prints 3. 
