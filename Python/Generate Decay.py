import Brence as br
import Decay

d = Decay.Decay()
print d.Decay["232Th"]
#quit()

f = br.getscriptdir()+"Decay.csv"
print f
n = br.readCSV(f)
ls = []
#(Probability1,Half_Life,Type,Energy,"Product Name")
for i in n:
    j = [i[0],[1,(i[2],i[4],i[3],i[5],i[6])]]
    ls.append(j)
    #print i
    #print j
ls.sort()
ls2 =[]
for i in range(len(ls)-1):
    if ls[i][0] == ls[i-1][0]:
        #print "oops",ls[i][0]
        #print ls2[-1]
        ls2[-1][1].append(tuple(ls[i][1][1]))
        ls2[-1][1][0] = 2
        ls2[-1] = tuple(ls2[-1])
        #print ls2[-1]
    else:
        ls2.append(ls[i])
        
dic = dict(ls2)
for i in dic:
    dic[i] = tuple(dic[i])
    print "\t\""+i+"\":",
    print dic[i],
    print ","
