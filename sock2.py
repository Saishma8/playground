import socket
import re

page = raw_input("Enter page:")
temp = re.findall('://(.*?)[/?]',page)
page1 = temp[0]

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((page1,80))

mysock.send('GET %s HTTP\1.0\n\n' %(page,))

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print data

mysock.close()

