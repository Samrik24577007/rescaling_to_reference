import sys
from collections import defaultdict
import pandas as pd
df_q=pd.read_csv(sys.argv[1],sep="\t",header=None)
df_r=pd.read_csv(sys.argv[2],sep="\t",header=None)
q_len=list(df_q[0])
q_nfreq=list(df_q[2])
q_freq=list(df_q[1])
r_len=list(df_r[0])
r_nfreq=list(df_r[1])
max_diff=0

for i in range(len(r_len)):
	if r_len[i] in q_len:
		a=q_len.index(r_len[i])
		b=r_nfreq[i] - q_nfreq[a]
		if abs(b) >= max_diff: 
			max_diff,index_q,index_r=b,a,i
			
sampling={}
for i in range(len(r_len)):
	c=(r_nfreq[i]/r_nfreq[index_r])*q_freq[index_q]
	if r_len[i] in q_len:
		a=q_len.index(r_len[i])
		if round(c) > q_freq[a]:
			sampling[r_len[i]]=q_freq[a]
		else:
			sampling[r_len[i]]=round(c)

for length in sampling:
	print(length ,'\t',sampling[length])


	
