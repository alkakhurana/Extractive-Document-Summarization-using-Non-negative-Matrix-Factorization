Extractive Document Summarization using Non-negative Matrix Factorization

This repository contains Python (v 3.6) scripts for implementation of NNDSVD-TR and NNDSVD-TP methods for Single document extractive summarization.

**NNDSVD-TR**: Term-oriented Extractive Summarization
**NNDSVD-TP**: Topic-oriented Extractive Summarization


**Author**:  Alka Khurana
**Acknowledgement**: Vasudha Bhatnagar

**Description:**
Both the algorithms generate score for each sentence (TR-score, TP-score) in the input document and present the sentences in the descending order of their scores.
Top scoring sentences are included in the document summary until required summary length is complete. 


**Pipeline:**
1. Clone the complete directory.
2. Put the documents in the Documents folder for which summary is to be generated.
3. Run Preprocessing.py for pre-processing the input documents.
4. Run NNDSVD_TR.py  for generating the summary of the text using Term-oriented method. Run NNDSVD_TP.py  for generating the summary of the text using Topic-oriented method.
5. In all the .py files, change the current directory to working directory of your system.
