#!/bin/sh

# reads to REMOVE (-F):
# unmapped reads                4 +
# supplementary alignment    2048 =
#                           -------
# total                      2052

samtools view -F 2052 results.sam > filtered_res.sam