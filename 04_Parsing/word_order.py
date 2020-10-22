#!/usr/bin/env python3

import sys

ov = 0
vo = 0

with open(sys.argv[1], 'r', encoding='utf-8') as file:
    for line in file:
        if (not line.startswith("#")) and (line.strip()):
            words = line.split()
            if words[7] == 'obj':
                verb = int(words[6])
                if int(words[0]) > verb:
                    vo+=1
                else:
                    ov+=1

print(ov/(vo+ov))
print(vo/(vo+ov))