import re

f1 = open('qapair.txt','r')
f2 = open('vote_sum.txt','w')

sum_bst = 0
cnt_bst = 0
avg_bst = 0.0

sum_sec = 0
cnt_sec = 0
avg_sec = 0.0


sum_thr = 0
cnt_thr = 0
avg_thr = 0.0

sum_four = 0
cnt_four = 0
avg_four = 0.0

sum_fif = 0
cnt_fif = 0
avg_fif = 0.0


sum_six = 0
cnt_six = 0
avg_six = 0.0

sum_sev = 0
cnt_sev = 0
avg_sev = 0.0

sum_eig = 0
cnt_eig = 0
avg_eig = 0.0

sum_nin = 0
cnt_nin = 0
avg_nin = 0.0

sum_ten = 0
cnt_ten = 0
avg_tem = 0.0

for line in f1:
    info = line.split(',')
    
    try :
        bst_vote = info[1]
        print bst_vote
        sum_bst += int(bst_vote)
        cnt_bst = cnt_bst + 1
        
        sec_vote = info[2]
        sum_sec += int(sec_vote)
        cnt_sec = cnt_sec + 1

        thr_vote = info[3]
        sum_thr += int(thr_vote)
        cnt_thr = cnt_thr + 1

        four_vote = info[4]
        sum_four += int(four_vote)
        cnt_four = cnt_four + 1

        fif_vote = info[5]
        sum_fif += int(fif_vote)
        cnt_fif = cnt_fif + 1

        six_vote = info[6]
        sum_six += int(six_vote)
        cnt_six = cnt_six + 1

        sev_vote = info[7]
        sum_sev += int(sev_vote)
        cnt_sev = cnt_sev + 1

        eig_vote = info[8]
        sum_eig += int(eig_vote)
        cnt_eig = cnt_eig + 1

        nin_vote = info[9]
        sum_nin += int(nin_vote)
        cnt_nin = cnt_nin + 1
        
        ten_vote = info[10]
        sum_ten += int(ten_vote)
        cnt_ten = cnt_ten + 1

    except IndexError:
        pass 

avg_bst = float(sum_bst)/cnt_bst
print sum_bst
print cnt_bst
print avg_bst
f2.write('Sum votes of best answer:'+str(sum_bst)+
         ' Number of best answer:'+str(cnt_bst)+
         ' Average votes of best answer:'+str(avg_bst)+'\n')

avg_sec = float(sum_sec)/cnt_sec
print sum_sec
print cnt_sec
print avg_sec
f2.write('Sum votes of second answer:'+str(sum_sec)+
         ' Number of second answer:'+str(cnt_sec)+
         ' Average votes of second answer:'+str(avg_sec)+'\n')


avg_thr = float(sum_thr)/cnt_thr
print sum_thr
print cnt_thr
f2.write('Sum votes of third answer:'+str(sum_thr)+
         ' Number of third answer:'+str(cnt_thr)+
         ' Average votes of third answer:'+str(avg_thr)+'\n')


avg_four = float(sum_four)/cnt_four
print sum_four        
print cnt_four
f2.write('Sum votes of 4th answer:'+str(sum_four)+
         ' Number of 4th answer:'+str(cnt_four)+
         ' Average votes of 4th answer:'+str(avg_four)+'\n')

avg_fif = float(sum_fif)/cnt_fif
print sum_fif
print cnt_fif
f2.write('Sum votes of 5th answer:'+str(sum_fif)+
         ' Number of 5th answer:'+str(cnt_fif)+
         ' Average votes of 5th answer:'+str(avg_fif)+'\n')


avg_six = float(sum_six)/cnt_six
print sum_six
print cnt_six
f2.write('Sum votes of 6th answer:'+str(sum_six)+
         ' Number of 6th answer:'+str(cnt_six)+
         ' Average votes of 6th answer:'+str(avg_six)+'\n')


avg_sev = float(sum_sev)/cnt_sev
print sum_sev
print cnt_sev
f2.write('Sum votes of 7th answer:'+str(sum_sev)+
         ' Number of 7th answer:'+str(cnt_sev)+
         ' Average votes of 7th answer:'+str(avg_sev)+'\n')

avg_eig = float(sum_eig)/cnt_eig
print sum_eig
print cnt_eig
f2.write('Sum votes of 8th answer:'+str(sum_eig)+
         ' Number of 8th answer:'+str(cnt_eig)+
         ' Average votes of 8th answer:'+str(avg_eig)+'\n')

avg_nin = float(sum_nin)/cnt_nin
print sum_nin
print cnt_nin
f2.write('Sum votes of 9th answer:'+str(sum_nin)+
         ' Number of 9th answer:'+str(cnt_nin)+
         ' Average votes of 9th answer:'+str(avg_nin)+'\n')


avg_ten = float(sum_ten)/cnt_ten
print sum_ten
print cnt_ten
f2.write('Sum votes of 10th answer:'+str(sum_ten)+
        ' Number of 10th answer:'+str(cnt_ten)+
        ' Average votes of 10th answer:'+str(avg_ten)+'\n')



f1.close()
f2.close()
