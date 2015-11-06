import re

f0 = open('q0.json', 'a+')
f1 = open('q1.json', 'r')
f2 = open('q2.json', 'r')
f3 = open('q3.json', 'r')


for line in f3:
    print line
    f0.write(line)

f0.close()
f1.close()
f2.close()
f3.close()
