"""
Lab 3, exercise 2 (part 2): Raw read count for protein coding genes
Bioinformatics @ Politecnico di Torino
Author: Silvia Giammarinaro

"""

# python ex2_b.py filtered_res.sam chr10_chr18.txt 

import sys
import pandas as pd
from collections import defaultdict

if __name__ == "__main__":
    input_sam_file = sys.argv[1]
    input_gtf_file = sys.argv[2]
    data = pd.DataFrame(columns=['chr', 'gene_name', 'start', 'end'])
    solution = pd.DataFrame(columns=['gene_name', 'count'])
    with open(input_gtf_file, 'r') as lines:
        for i, line in enumerate(lines):
            gene_name = line.split(";")[2].split()[1].replace('"',"")
            chr = line.split()[0]
            start = int(line.split()[3])
            end = int(line.split()[4])
            # add one row to the dataframe
            data = data.append(dict(zip(data.columns, [chr, gene_name, start, end])), ignore_index=True)

    #data.to_csv('data.csv', index=False)

    with open(input_sam_file, 'r') as lines:
        for i, line in enumerate(lines):
            chr = line.split()[2]
            pos = int(line.split()[3])
            #print("Pos: ", pos)
            chr_rows = data.loc[data["chr"].str.match(chr)]
            matched_rows = chr_rows.loc[(chr_rows['start'] <= pos) & (chr_rows['end'] >= pos)]
            #print("Matched rows: ", matched_rows)
            #print(len(matched_rows))
            if len(matched_rows) > 0: # match found
                #print("----------- MATCH FOUND -----------")
                gene = matched_rows['gene_name'].values[0]
                #print(gene)
                gene_row = solution.loc[solution['gene_name'].str.match(gene)]
                # gene already in the dataframe --> +1
                if len(gene_row) == 1 : 
                    gene_row['count'] +=1 
                else: # new gene inserted in the dataframe--> 1
                    solution = solution.append(dict(zip(solution.columns, [gene, 1])), ignore_index=True)
    
    #print(solution.head())
    solution.to_csv('solution.csv', index=False)
            
            
