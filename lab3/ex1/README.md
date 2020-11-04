# Exercise 1: Search for SNP and deletions in a sample

* [`prepare_vcf.sh`](./prepare_vcf.sh):  
  * Convert SAM file obtained in LAB2  `results.sam` to BAM.
  * Sort BAM to make the following process faster.
  * Use bcftools to obtain a VCF file.
* [`ex1.py`](./ex1.py):
  * Write a Python program to parse the VCF file and obtain only Single Nucleotides Polymorphism (SNP) for which the information is complete.
  * Write a Python program to parse the VCF file and obtain only Insertions or Deletions (INDEL) for which the information is complete
