"""
Lab 1, exercise 3: Fasta comparison
Bioinformatics @ Politecnico di Torino
Author: Silvia Giammarinaro

"""

# python ex2.py input_file1 input_file2 output_file
# The input files are fasta file, assume correct format and no duplicated reads
# The output file contains the reads in commons between the input files

# Example
# python ex3.py file1.fa file2.fa output_ex3.txt


import sys 

def read_file(seq_dict, input_name):
    with open(input_name, 'r') as lines:
        for i, line in enumerate(lines):
            if i % 2 == 1:
                if line in seq_dict:
                    seq_dict[line].append(readID)
                else:
                    seq_dict[line] = [readID]
            else:
                readID = line[1:-1]


if __name__ == "__main__":
    input_file1 = sys.argv[1]
    input_file2 = sys.argv[2]
    output_file = sys.argv[3]
    sequences = {}
    read_file(sequences, input_file1)
    read_file(sequences, input_file2)

    with open(output_file, 'w') as f:
        f.write("COMPARISON RESULTS \n")
        for key, values in sequences.items():
            if len(values) > 1:
                f.write(values[0] + "---" + values[1] + "\n")
        



    
