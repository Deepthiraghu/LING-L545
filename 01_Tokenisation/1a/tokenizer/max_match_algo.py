import sys

def maxmatch(sentence, jap_dict):
	if sentence == '':
		return([])

	for i in range(len(sentence),0,-1):
		first = sentence[:i+1]
		remain = sentence[i+1:]
		if first in jap_dict:
			return([first, remain])

	first = sentence[0]
	remain = sentence[1:]
	return([first, remain])

jap_dict = open('jap_dict.txt').read().split('\n')

for sentence in sys.stdin.readlines():
	while sentence:
		word = maxmatch(sentence, jap_dict)
		print(word[0]+' ')
		sentence = word[1]
