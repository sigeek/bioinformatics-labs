"""
Lab 1, exercise 1: Random fasta and fastq file generator
Bioinformatics @ Politecnico di Torino
Author: Silvia Giammarinaro

"""

# python ex1.py output_file nReads probA probT probC probG
# Output file extension could be could be fa (fasta) or fq (fastq)

# Example
# python ex1.py output_ex1.fa 100 30 30 30 10

import numpy as np

class generator:

    def __init__(self, output_file, nRead, probA, probT, probC, probG):
        self.__output_file = output_file
        self.__nReads = nReads
        self.__probs = np.array([probA, probT, probC, probG])
        self.__probs = self.__probs/self.__probs.sum()
        self.__bases = np.array(['A', 'T', 'C', 'G'])
        
    def __getRandomBase(self):
        return np.random.choice(self.__bases, p = self.__probs)
    
    def __getRandomQualityScore(self):
        return chr(np.random.choice(np.arange(33, 127))) #Sanger format
    
    def generateFasta(self, bp):
        with open(self.__output_file, 'w') as f:
            for i in range(self.__nReads):
                f.write('>' + str(i) + '\n')
                for _ in range(bp):
                    f.write(self.__getRandomBase())
                f.write('\n')
                
    def generateFastq(self, bp):
        with open(self.__output_file, 'w') as f:
            for i in range(self.__nReads):
                f.write('@' + str(i) + '\n')
                for _ in range(bp):
                    f.write(self.__getRandomBase())
                f.write('\n')
                f.write('+' + str(i) + '\n')
                for _ in range(bp):
                    f.write(self.__getRandomQualityScore())
                f.write('\n')

import sys 

if __name__ == "__main__":
    
    output_file = sys.argv[1]
    nReads = int(sys.argv[2])
    probA = float(sys.argv[3])
    probT = float(sys.argv[4])
    probC = float(sys.argv[5])
    probG = float(sys.argv[6])
    fg = generator(output_file, nReads, probA, probT, probC, probG)
    bp = 50
    
    if sys.argv[1][-1] == 'a':
        fg.generateFasta(bp)
        
    elif sys.argv[1][-1] == 'q':
        fg.generateFastq(bp)

