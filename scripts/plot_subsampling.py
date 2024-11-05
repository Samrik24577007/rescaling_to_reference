import sys
from matplotlib import pyplot as plt
import pandas as pd
repeat=sys.argv[1]
sub_dist=sys.argv[2]
ref_dist=sys.argv[3]
q_dist=sys.argv[4]
sample=sys.argv[5]
reference=sys.argv[6]
sub_dist_list=sub_dist.strip().split(" ")
df_ref=pd.read_csv(sys.argv[3],sep="\t", header=None)
df_q=pd.read_csv(sys.argv[4],sep="\t",header=None)

for path in sub_dist_list:
	df_sub=pd.read_csv(path,sep="\t",header=None)
	plt.scatter(df_sub[0],df_sub[2],label=str(sub_dist_list.index(path)+1))

plt.scatter(df_q[0],df_q[2],label="Query")
plt.scatter(df_ref[0],df_ref[1],label="Reference")
plt.xlabel("length")
plt.ylabel("normalised frequency")

plt.legend()
plt.savefig("plotted_subsampled_files/" + sample + "_" + reference + "_subsampled_" + repeat + ".png")
plt.show()

	
