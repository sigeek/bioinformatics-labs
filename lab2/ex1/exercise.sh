#!/bin/sh
cd ./Lab2
conda install -c bioconda bwa
#unzip files
gzip -d *.fa.gz 
#concatenate them
cat *.chromosome.*.fa > reference_chr10_chr18.fa
#cat chr*.fa > reference_chr10_chr18.fa  
#create folder for the bwa index
mkdir /BWA 
# add permissions to folder
sudo chmod a+rwx /BWA
# create a bwa index for the reference sequence reference_chr10_chr18.fa
bwa index -p ./BWA/ reference_chr10_chr18.fa
# alignment on mate_1 and mate_2
bwa mem ./BWA/ mate_1.fq mate_2.fq > results.sam


