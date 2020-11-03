# Exercise 3: Run BWA
Perform the Barrow Willow Alignment on real human data. We will use only two chromosomes, downloadable from here: 
* chr 10: [`ftp://ftp.ensembl.org/pub/release-92/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.10.fa.gz`](ftp://ftp.ensembl.org/pub/release-92/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.10.fa.gz)
* chr 18: [`ftp://ftp.ensembl.org/pub/release-92/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.18.fa.gz`](ftp://ftp.ensembl.org/pub/release-92/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.18.fa.gz)
* After the downloads, we unzip and concatenate them. The concatenation will be our reference genome.
* Create a bwa index for the reference sequence.
* Perfome Perform the alignment of mate_1.fq and mate_2.fq (both present in this folder)
