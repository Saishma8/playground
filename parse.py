fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print "Invalid file name"
    exit()

count = 0
lst = []

for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        print line.split()[1]
        count = count + 1     

print "There were", count, "lines in the file with From as the first word"
