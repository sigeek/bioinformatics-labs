# Exercise 1: Random fasta and fastq file generator
Write a python program that generates both fasta and fastq files containing reads with the following characteristics
- Read id contains a progressive number starting from 0
- Sequences have length 50 bp
- Bases are randomly generated using a A,T,C,G alphabet, but probability of each base for each read should be given from the command line as a set of numbers probA probT probC probG
- The number of reads should be passed as an argument from the command line
- The name of the fasta fastq file should be passed as an argument from the command line
- For fastq files only the quality of each base is randomly selected
