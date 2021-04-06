"""
Lab 5, exercise 1: T-test to perform differential gene expression analysis
Bioinformatics @ Politecnico di Torino
Author: Silvia Giammarinaro

"""

# python ex1.py

import pandas as pd
import scipy.stats as stats
import numpy as np

if __name__ == "__main__":
    data = pd.read_csv("dataset_LUMINAL_A_B.csv")
    input_file = "Homo_sapiens.GRCh38.95.gtf"
    output_file = "reduced_dataset.csv"

    #print(data.head())
    n_genes = data.shape[1]-1
    p_value_bonferroni = 0.05/n_genes
    print("Number of genes: ", n_genes)
    print("P Value Bonferroni ", p_value_bonferroni)
    lum_a_samples = data.loc[data['l'].str.match('Luminal A')] #select rows labelled as 'Luminal A'
    lum_a_samples = lum_a_samples.loc[:, lum_a_samples.columns != 'l'] #drop label column
    lum_b_samples = data.loc[data['l'].str.match('Luminal B')]
    lum_b_samples = lum_b_samples.loc[:, lum_b_samples.columns != 'l']
    print("Luminal A samples: ", len(lum_a_samples))
    print("Luminal B samples: ", len(lum_b_samples))

    #list containing the differentially expresssed genes with ENSEMBL notation
    diff_exp_genes_ensembl_raw = [] 
    for column in lum_a_samples:
        lum_a = lum_a_samples[column]
        lum_b = lum_b_samples[column]
        t_value, p_value= stats.ttest_ind(np.array(lum_a), np.array(lum_b), equal_var=False)
        if p_value <= p_value_bonferroni:
            diff_exp_genes_ensembl_raw.append(column)

    print("Number of differentially expressed genes:", len(diff_exp_genes_ensembl_raw))

    
    # remove the second part after the "." and create a dictionary
    # key: gene id
    # value: bool value -> False: related gene name not already found in the gtf file
    #                    -> True: related gene name found
    diff_exp_genes_ensembl = {}
    for gene in diff_exp_genes_ensembl_raw:
        gene = gene.split(".")[0]
        diff_exp_genes_ensembl[gene] = False
    print(diff_exp_genes_ensembl)

    diff_exp_genes = set()
    with open(input_file, 'r') as lines:
        for i, line in enumerate(lines):
            if line.startswith('#'):
                continue
            else:
                columns = line.split()
                gene_id = columns[9].strip("\";")
                gene_name = columns[13].strip("\";")
                if gene_id in diff_exp_genes_ensembl.keys():
                    if diff_exp_genes_ensembl[gene_id] == False:
                        diff_exp_genes.add(gene_name)
                        diff_exp_genes_ensembl[gene_id] = True

    print("Set diffentially expresssed genes with common name: ", diff_exp_genes)

    # add manually the label column 
    columns_list = diff_exp_genes_ensembl_raw
    columns_list.append('l')
    reduced_dataset = data[data.columns.intersection(columns_list)]
    print("Reduced dataset shape: ", reduced_dataset.shape)
    reduced_dataset.to_csv(output_file, index=False)


    

