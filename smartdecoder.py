#!/usr/bin/python
# Fast hack to convert a string containing ascii, hexa and unicode all mixed to ascii.
# Author: Sebastian Garcia, eldraco@gmail.com
import sys

# example string "\x64\u0065\u006cay\u0042\x65\u0074\u0077\u0065e\x6e"
a = sys.stdin.readline()
a = a.strip()
n = ''
i=0
while i < len(a):
    if a[i] == '\\':
        # unicode or hexa
        if a[i+1] == 'x':
            temp = a[i+2:i+4].decode("hex")
            #print '{}: hexa'.format(temp)
            n += temp
            i += 4
        elif a[i+1] == 'u':
            # unicode
            temp = unicode(a[i:i+6])
            #print '{}: uni'.format(temp.decode('unicode-escape'))
            n += temp.decode('unicode-escape')
            i += 6
    else:
        #print '{}: ascii'.format(a[i])
        n += a[i]
        i+=1
print n
