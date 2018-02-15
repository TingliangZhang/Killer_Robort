import sys
filename=sys.argv[0]
linenum=0
with open(filename,'r',encoding='utf8') as f:
        for line in f:
                linenum +=1
                print(linenum,":",line)
f.close()
input()
