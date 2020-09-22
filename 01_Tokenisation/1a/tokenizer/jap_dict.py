input_file = open('ja_gsd-ud-test.conllu')
line = ''
dict = []
while True:
	line = input_file.readline()
	if not line: 
		break
	line = line.strip('\n')
	if line == '':
		continue
	if line[0]=='#':
		continue
	line = line.split()
	dict.append(line[1])	
dictionary_set = set(dict)
dictionary_list = list(dictionary_set)

output = open('jap_dict.txt','w')

for i in range(0,len(dictionary_list)):
	output.write(dictionary_list[i]+'\n')

input_file.close()
output.close()
