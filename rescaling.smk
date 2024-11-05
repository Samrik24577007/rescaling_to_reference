import sys
import pandas as pd
run_df=pd.read_csv("data/run_metadata.tsv",sep="\t",header="infer")
sample_df=pd.read_csv("data/samples.tsv",sep="\t",header="infer")
print(run_df)
print(sample_df)
run_df.index=run_df["run"]
sample_df.index=sample_df["sample"]
def get_all_runs_for_a_sample(wildcards):
	all_runs=sample_df.loc[wildcards.sample,"runs"].split(",")
	print(all_runs)
	run_path_list=[]
	for r in all_runs:
		p=run_df.loc[r,"file_path"]
		print(p)
		run_path_list.append(p)
	return run_path_list
rule query_dist:
	input:
		all_runs= lambda wildcards: get_all_runs_for_a_sample(wildcards)
	output:
		"query_freq_dist/{sample}_freq_dist.tsv"
	
	shell:
		"zcat {input.all_runs} | python scripts/query_dist.py > {output}"
rule sampling_freq:
	input:
		query_dist="query_freq_dist/{sample}_freq_dist.tsv",
		refer_dist="{reference}.hist"
	output:
		"sampling_list/{sample}_{reference}_sampling_freq.tsv"
	
	shell:
		"python scripts/sampling_dist.py {input.query_dist} {input.refer_dist} > {output}"
rule subsampled_files:
	input:
		all_runs=lambda wildcards: get_all_runs_for_a_sample(wildcards),
		subsampling_list="sampling_list/{sample}_{reference}_sampling_freq.tsv"
	output:
		"subsampled_files/{sample}_{reference}_subsampled_rep_{number}.bed"
	shell:  
		"zcat {input.all_runs} | shuf  | python scripts/subsampling_file.py {input.subsampling_list} {wildcards.reference}  > {output} "

rule subsampled_distribution_files:
	input:
		"subsampled_files/{sample}_{reference}_subsampled_rep_{number}.bed"
	output:
		"subsampled_files_freq/{sample}_{reference}_subsampled_rep_{number}.tsv"
	shell:
		"cat {input} | python scripts/query_dist.py > {output}"
rule plotting_subsampled_files:
	input:
		subsample_dist=lambda wildcards : ["subsampled_files_freq/{sample}_{reference}_subsampled_rep_{number}.tsv".format(sample=wildcards.sample,reference=wildcards.reference, number=c) for c in range(1,int(wildcards.subsampling_num) + 1)],
		reference_dist="{reference}.hist" ,
		query_dist="query_freq_dist/{sample}_freq_dist.tsv"
	output:
		"plotted_subsampled_files/{sample}_{reference}_subsampled_{subsampling_num}.png"
	shell:
		"python scripts/plot_subsampling.py {wildcards.subsampling_num} \"{input.subsample_dist}\" {input.reference_dist} {input.query_dist} {wildcards.sample} {wildcards.reference}"
	
