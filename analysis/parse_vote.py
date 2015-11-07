import re
import json

#f1 = open('a1.json', 'r')
#f2 = open('qapair.txt', 'w')



#line = f1.readline()
#print line 

path = 'a1.json'
a = open(path)
b = a.read()
#print b[0]
records = json.loads(b)
#print records[0]
#print type(records[0]['vote_up'][0])
#print records[0]['vote_down'][0]

for i in range(0,10):
    vd = records[i]['vote_down']
    vp = records[i]['vote_up']
    print vp
    print type(vp)
    length = len(vp)
    print length
    for j in range(0,length):
        print j
        vote = int(vp[j]) - int(vd[j])
        print vote

#    print vote[j]


#records = [json.loads(line) for line in open(path)]

#print records[0]


#f1.close()
#f2.close()
