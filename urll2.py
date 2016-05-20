import urllib

page = raw_input("Enter page:")

fh = urllib.urlopen(page)

for line in fh:
    print line.strip()

