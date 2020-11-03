# Exercise 3: Fasta comparison
Write a python program to compare two fasta files The two fasta files are passed as first and second argument from the command line.
The two fasta files have the following characteristics:
- The fasta format of the two files is correct (no need to check the format)
- Each read can take up one or multiple lines
- Each input file does not contain duplicated reads (i.e. identical reads)
The program must write as output a third fasta file containing only the reads that are in common
between the input files The read ids in the output file should be composed by the read id of the
first file concatenated with the read id of the second file.

