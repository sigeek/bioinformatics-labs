#!/bin/sh

# sh run_bwa.sh bwa_folder genomeref mate_1 mate_2 outputdata
# sh ex4.sh ./BWA_index/ reference_chr10_chr18.fa mate_1.fq mate_2.fq res.sam

echo "Creating folder for the BWA index..."
mkdir $1
sudo chmod a+rwx $1
echo "BWA initializing..."
bwa index -p $1 $2
echo "Creating BWA index..."
echo "Starting BWA aligner..."
bwa mem $1 $3 $4 > $5

