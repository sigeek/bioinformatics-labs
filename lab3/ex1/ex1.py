"""
Lab 3, exercise 1: Search for SNP and deletions in a sample
Bioinformatics @ Politecnico di Torino
Author: Silvia Giammarinaro

"""
# before starting, execute prepare_vcf.sh

# python ex1.py sort_results.vcf

import sys 
import re

if __name__ == "__main__":
    complete_SNP_rows = []
    INDEL_rows = []
    input_file = sys.argv[1]
    with open(input_file, 'r') as lines:
        for i, line in enumerate(lines):
            if line.startswith('##'):
                continue
            elif line.startswith('#'):
                continue
            else:
                columns = line.split("\t")
                ALT = columns[4]
                INFO = columns[7]
                pattern = re.compile("^[ACGT].")
                if pattern.match(ALT):
                    complete_SNP_rows.append(line)
                    if "INDEL" in INFO:
                        INDEL_rows.append(line)


    #print(complete_SNP_rows)
    #print(INDEL_rows)