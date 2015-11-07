import re
import json


f = open('qapair.txt', 'w')
#line = f1.readline()
#print line 

path = 'a1.json'
a = open(path)
b = a.read()
records = json.loads(b)
#vote = []
print records[0]
print len(records[0])
#print type(records[0]['vote_up'][0])
#print records[0]['vote_down'][0]

for i in range(0,1972):
    vote = []
    qid = records[i]['related_id']
    f.write(qid)
    if len(records[i]) > 1:
        vd = records[i]['vote_down']
        vp = records[i]['vote_up']
        #print vp
        #print vd
        length = len(vp)
        for j in range(0,length):
            v = int(vp[j]) - int(vd[j])
            f.write(','+str(v))
            vote.append(v) 
        print vote
    f.write('\n')
    f.flush()
    
f.close()
