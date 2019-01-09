#PREREQUISITES
#Install Pandas
#Provide a header to your blast results, give specifically names 'evalue' and 'qcovs' for evalue and query coverage column of your blast output.
#import pandas
import pandas as pd
#import csv
import csv
#Read blast results file
blast_results = pd.read_csv("/home/scis/blastdb/test.out", sep = '\t', index_col = False)
#Provide evalue cutoff you want to apply.
evalue_cutoff = 1e-05
#Provide query coverage cutoff you want to apply
qcovs_cutoff = 50
#Parsing step
cutoffs = ((blast_results['evalue'] <= evalue_cutoff) & (blast_results['qcovs'] >= qcovs_cutoff))
#save output into a dataframe
parsed_output = blast_results[cutoffs]
#write the results to a csv
parsed_output.to_csv("parsed_blast.csv", sep='\t')
