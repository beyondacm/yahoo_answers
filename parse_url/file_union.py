import re

f0 = open('q0.json', 'a+')
#f1 = open('q1.json', 'r')
#f2 = open('q2.json', 'r')
#f3 = open('q3.json', 'r')
#f4 = open('q4.json', 'r')
#f5 = open('q5.json', 'r')
#f6 = open('q6.json', 'r')
#f7 = open('q7.json', 'r')
f8 = open('q8.json', 'r')

for line in f8:
    print line
    f0.write(line)

f0.close()
#f1.close()
#f2.close()
#f3.close()
#f5.close()
#f6.close()
#f7.close()
f8.close()
