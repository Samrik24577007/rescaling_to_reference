Shuf.a.bed.gz and shuf.b.bed.gz should be downloaded in data directory
The data also contains run_metadata.tsv and samples.tsv that contains file_paths of different runs and list of different runs under a sample X
The reference.hist file is there in the working directory.
the rule query_dist takes inputs as shuf.a.bed.gz and shuf.b.bed.gz and gives the each fragment length, its frequency and normalised frequency in the output file query_freq_dist/{sample}_freq_dist.tsv
The rule sampling_freq takes input as the output file of previous rule and reference.hist to find the sampling list to be sampled out from query file to rescale it to the reference distribution.
The output file is sampling_list/{sample}_{reference}_sampling_freq.tsv
The rule subsampled_files takes input as the shuf.a.bed.gz , shuf.b.bed.gz and the previous rule output to sample out randomly from the shuf files to maintaining the frequency to form different subsampled_files/{sample}_{reference}_subsampled_rep_{number}.bed files
As the output bed files are too big , we couldn't include those
The subsampled_distribution_files rule takes the subsampled bed file output from the previous rule and gives their normalised frequency distribution into corresponding subsampled_files_freq/{sample}_{reference}_subsampled_rep_{number}.tsv
The rule plotting_subsampled_files takes all the previous rule output subsampled file normalised frequency distributions, reference.hist and output from rule query_dist to plot them in one graph plotted_subsampled_files/{sample}_{reference}_subsampled_{subsampling_num}.png 
It takes the subsampling_num as input from user
To get the output file, we have to run "snakemake -p -j1 --snakefile rescaling.smk plotted_subsampled_files/X_reference_subsampled_3.png
