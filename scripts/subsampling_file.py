import sys
import pandas as pd
from collections import defaultdict
s_df=pd.read_csv(sys.argv[1],sep="\t",header=None)
s_len=list(s_df[0])
s_freq=list(s_df[1])

fp_dict=defaultdict(lambda:0)
for i in range(len(s_len)):
	fp_dict[str(s_len[i])]+=int(s_freq[i])
#for i in range(1,number+1):
#	fp_dict[i]=open("subsampled_files/" + sample +  "_" + reference +"_subsampled_rep_" + i +".bed","w")

for line in sys.stdin:
	l_items=line.strip().split("\t")
	length=int(l_items[2]) - int(l_items[1])
	if str(length) in fp_dict:
		freq=fp_dict[str(length)]
		if int(freq) > 0:
			print(line)
			fp_dict[str(length)]+= -1
			
