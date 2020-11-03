#!/bin/sh

conda install -c bioconda samtools
conda install -c bioconda bcftools

gunzip -d Homo_sapiens.GRCh38.95.gtf.gz

samtools view -S -b results.sam > results.bam
samtools sort results.bam > sort_results.bam
bcftools mpileup --fasta-ref reference_chr10_chr18.fa sort_results.bam > sort_results.vcf