import re
fh = open('regex_sum_272363.txt')

lst = []
tot = 0

for line in fh:
    line.rsplit()
    y = re.findall('[0-9]+', line)
    for i in y:
        tot = tot + int(i)

print tot
#for i in lst:
 #   tot = tot + int(i)
    
#print total
