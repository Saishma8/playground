xfile = open('Sam.py', 'r')

for line in xfile:
    line = line.rstrip()
    print line

xfile.close()
