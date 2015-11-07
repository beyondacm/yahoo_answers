import re


fin = open('urls.txt','r')
fout1 = open('urls_01.txt','w')
fout2 = open('urls_02.txt','w')
fout3 = open('urls_03.txt','w')
fout4 = open('urls_04.txt','w')
fout5 = open('urls_05.txt','w')

line_count = 0
line = fin.readline()

while line is not None:
    if line_count <= 2000:
        fout1.write(line)
    elif line_count >2000 and line_count <= 4000:
        fout2.write(line)
    elif line_count >4000 and line_count <= 6000:
        fout3.write(line)
    elif line_count >6000 and line_count <= 8000:
        fout4.write(line)
    elif line_count >8000:
        fout5.write(line)
    line_count = line_count + 1
    print line
    line = fin.readline()

fin.close()
fout1.close()
fout2.close()
fout3.close()
fout4.close()
fout5.close()















    
