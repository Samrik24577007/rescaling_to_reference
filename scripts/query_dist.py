
import sys
from collections import defaultdict
DS_c=defaultdict(lambda:0)

#chr10	32795245	32795315	70	.	+
#chr11	95864728	95864770	42	.	+
#chr16	32027808	32027880	72	.	+
#chr4	76608451	76608515	64	.	+


#chr20	27154210	27154270	A00738:475:HCY7JDSX5:4:2318:9082:4789_ACAAATAGTCAC	60	-
#chr10	7187015	7187080	A00738:475:HCY7JDSX5:4:1671:17626:21809_CAGGCAAGGTTC	65	+
#chr14_GL000225v1_random	101294	101344	A00738:475:HCY7JDSX5:4:2218:10493:32189_GAACAATTACCC	50	+

for line in sys.stdin:
	l_items=line.strip().split("\t")
	if len(l_items) > 1:
		DS_c[int(l_items[2])-int(l_items[1])]+=1
total=0	
for length in DS_c:
	total+=DS_c[length]
for length in DS_c:
	print(length,"\t",DS_c[length] , "\t",DS_c[length]/total)


