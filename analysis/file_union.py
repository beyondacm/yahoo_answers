import re

tempfiles = ['qapair1.txt','qapair2.txt','qapair3.txt','qapair4.txt','qapair5.txt']
f = open('qapair.txt', 'w')
with open('qapair.txt','w') as fo:
    for tempfile in tempfiles:
        with open(tempfile,'r') as fi:
            fo.write(fi.read())

print 'finished' 
    
 
