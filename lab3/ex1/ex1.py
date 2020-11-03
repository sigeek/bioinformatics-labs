"""
Lab 3, exercise 1: Search for SNP and deletions in a sample
Bioinformatics @ Politecnico di Torino
Author: Silvia Giammarinaro

"""
# before starting, execute prepare_vcf.sh

# python ex1.py sort_results.vcf

import sys 
import pandas as pd

if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, 'r') as lines:
        for i, line in enumerate(lines):
            if line.startswith('##'):
                continue
            elif line.startswith('#'):
                header = line.split("\t")
            else:
                dataframe = pd.read_csv(lines, sep="\t+", names=header)
                #print(dataframe.head())

    complete_SNP_rows = dataframe.loc[dataframe["ALT"].str.match("^[ACGT].")]
    print("First 5 complete SNP rows")
    print(complete_SNP_rows.head())

    INDEL_rows = complete_SNP_rows.loc[complete_SNP_rows["INFO"].str.match("INDEL")]
    print("First 5 INDEL rows")
    print(INDEL_rows.head())