import psutil
from itertools import groupby
from operator import itemgetter

initial = psutil.net_connections(kind='tcp')
list1 = []
list2 = []
list3 = []
j = 0

for c in initial:
    if c.raddr and c.laddr and c.pid:
        locadd = "%s@%s" % (c.laddr)
        remadd = "%s@%s" % (c.raddr)
        lit = [c.pid, locadd, remadd, c.status]
        list1.append(lit)

list1.sort(key=itemgetter(0))

for elt, items in groupby(list1, itemgetter(0)):
    for i in items:
        list2.append(i)
        if i[0] == elt:
            j= j+1 
    dic = {"count":j, "conn": list2}
    list3.append(dic)
    j = 0
    list2 =[]
newlist = sorted(list3, key=lambda n: n['count'], reverse= True) 

print ("\"pid\",\"laddr\",\"raddr\",\"status\"")

for k in newlist:
    for m in k["conn"]:
        print str(m).strip('[]')
