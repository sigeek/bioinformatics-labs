## Lab 5: Machine Learning Basics

* [`Exercise 1`](ex1.py): T test to perform
differential gene expression analysis.

Using dataset_LUMINAL_A_B.csv, perform a differential gene expression analysis in order to find which genes are able to distinguish between breast cancer Luminal A subtype and
breast cancer Luminal B subtype.
Calculate t-value and p-value for each gene and select only genes for which p value < adjusted Bonferroni p-value.
Finally, convert differentially expressed genes from ENSEMBL notation to the common name (e.g.
ENSG00000268889 is AC008750).

Create now a reduced dataset (from now on referred to as
reduced_dataset.csv ) made up of all samples
with only differentially expressed genes (use common name notation).

* [`Exercise 2`](ex2.py): Use gene expression
data to create a classifier for Luminal A / Luminal B breast cancer subtypes

In order to create a Luminal A / Luminal B breast cancer classifier, consider two dataset:
dataset_LUMINAL_A_B.csv (the one we provided you) and reduced_dataset.csv (the one you created in
exercise 1).
1. Divide both dataset_LUMINAL_A_B.csv and reduced_dateset.csv into train set and test set;
2. Standardize features of both datasets by removing the mean and scaling to unit variance;
3. Perform the dimensionality reduction onto dataset.csv with PCA (principal component Analysis) using
80 features;
4. Train a KNN classifier onto the train set of dataset_LUMINAL_A_B.csv with PCA;
5. Test the classifier obtained at the previous step onto the test set of dataset_LUMINAL_A_B.csv;
6. Implement from scratch the following performance metrics: accuracy, precision and recall, F1 score.
Compare your results with performance metrics provided by sklearn.metrics;
7. Train and test a KNN classifier onto reduced_dataset.csv.

