import re

f1 = open('q0.json', 'r')
f2 = open('urls.txt', 'w+')

s = set()
t = set()

for line in f1:
    info = line.split('"')
    
    if len(info[3]) == 38 :
        #print len(info[3])
        #print info[3][6:9]
        if info[3].startswith('page', 6, 10):
            #print info[3][17:]
            qid = info[3][17:]
        elif info[3].startswith('qid', 6, 9):
            #print info[3][10:30]
            qid = info[3][10:31]
        
    elif len(info[3]) == 31:
        #print len(info[3])
        #print info[3][10:]
        qid = info[3][10:]

    elif len(info[3]) == 45:
        #print len(info[3])
        #print info[3][17:37]
        qid = info[3][17:38]
    elif len(info[3]) == 46:
        qid = info[3][18:39]
    
    print qid
    t.add(qid)
    
    #f2.write(qid+'\n')
    #f2.flush()

print len(t)
#print t
for e in t :
    print e
    f2.write('https://answers.yahoo.com/question/index?qid='+e+'&sort=V'+'\n')
    #f2.write('https://answers.yahoo.com/question/index?qid='+e+'&page=2&sort=V'+'\n')
    
f1.close()
f2.close()
