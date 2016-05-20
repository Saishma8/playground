name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
    
try:
    fh = open(name)
except:
    print "Invalid file"
    exit()
    
var1 = []  
freq = dict()
    
for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        temp = line.split()[5]
        var1.append(temp.split(":")[0])

for i in var1:
    freq[i] = freq.get(i,0) + 1
    
for i,j in sorted(freq.items()):
    print i,j

