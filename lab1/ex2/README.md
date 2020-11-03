# Exercise 2: Statistics extraction
Write a python program for extracting statistics from fasta fastq files. The program must take as a first argument from the command line the name of the input fasta file to be analyzed and write to an output text file (whose name is passed as a second argument from the command line) a summary of the computed statistics.
The following are the expected output statistics:
- Statistics of single bases across all the reads Number of A,T,C,G
- Number of reads having at least one low complexity sequence AAAAAA, TTTTTT, CCCCCC or GGGGGG
- Number of reads having the number of GC couples (so called GC content higher than a threshold GC_THRESHOLD passed as third argument from the command line
- For each read having a GC content higher than GC_THRESHOLD, report the read_id and the number of GC couples
