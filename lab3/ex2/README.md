# Exercise 2: Raw read count for protein coding genes

* Download the gtf file used from here: [`ftp://ftp.ensembl.org/pub/release-95/gtf/homo_sapiens/Homo_sapiens.GRCh38.95.gtf.gz`]
* [`ex2_a.py`](./ex2_a.py): Write a python program that parses the file `chr10_chr18.txt` and extract information about chromosome 10 and 18. Select only rows for which the feature is equal to gene and gene_biotype equal to protein_coding. 
* [`filter_sam_file.sh`](./filter_sam_file.sh): Use samtools view to filter unmapped reads and supplementary alignments from the SAM file you obtained in LAB 2 Save your results into a new SAM file `filtered_res.sam`
* [`ex2_b.py`](./ex2_b.py): Using information from the reduced SAM and gtf files, write a Python script to calculate the raw read count for each protein coding gene in chr 10 and chr 18
