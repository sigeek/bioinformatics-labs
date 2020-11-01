"""
Lab 1, exercise 2: Statistics extraction
Bioinformatics @ Politecnico di Torino
Author: Silvia Giammarinaro

"""

# python ex2.py input_file output_file GC_threshold
# The input file is a fasta file

# Example
# python ex2.py file1.fa output_ex2.txt 1

import sys 

if __name__ == "__main__":
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    GC_threshold = int(sys.argv[3])
    counterA = 0
    counterT = 0
    counterC = 0
    counterG = 0
    readsLowComplexitySeq = 0
    dictReadsGCCouples = {}

    with open(input_file, 'r') as lines:
        for i, line in enumerate(lines):
            if i % 2 == 1: #sequence line
                counterA += line.count('A')
                counterT += line.count('T')
                counterC += line.count('C')
                counterG += line.count('G')
                if 'AAAAAA' in line or 'TTTTT' in line or 'CCCCC' in line or 'GGGGG' in line: 
                    #one low complexity sequence found, update counter
                    readsLowComplexitySeq +=1
                GCcouples = line.count('GC')
                if GCcouples > GC_threshold:
                    dictReadsGCCouples[readID] = GCcouples
            else:
                readID = line[1:-1]

    # print statistics on output file
    with open(output_file, 'w') as f:
        f.write("STATISTICS RESULTS \n")
        f.write("Number of A bases: " + str(counterA) + "\n")
        f.write("Number of T bases: " + str(counterT) + "\n")
        f.write("Number of C bases: " + str(counterC) + "\n")
        f.write("Number of G bases: " + str(counterG) + "\n")
        f.write("Number of reads with at least one low complexity sequence: " + str(readsLowComplexitySeq) + "\n")
        f.write("Number of reads with GC couples higher than the threshold " + str(GC_threshold) + ": " + str(len(dictReadsGCCouples)) + "\n")
        for key, value in dictReadsGCCouples.items():
            f.write("Read ID: " + key + ", number of GC couples: " + str(value) + "\n")


                


    

