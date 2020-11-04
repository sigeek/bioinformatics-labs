"""
Lab 3, exercise 2 (part 1): Raw read count for protein coding genes
Bioinformatics @ Politecnico di Torino
Author: Silvia Giammarinaro

"""

# python ex2_a.py Homo_sapiens.GRCh38.95.gtf chr10_chr18.txt

import sys

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    chr10_chr18_desired_rows = []
    with open(output_file, 'w') as f:
        with open(input_file, 'r') as lines:
            for i, line in enumerate(lines):
                if line.startswith('#'):
                    continue
                else:
                    if line.startswith("10") or line.startswith("18"):
                        columns = line.split("\t")
                        feature = columns[2]
                        if feature == "gene":
                            if 'protein_coding' in line:
                                f.write(line)

    

