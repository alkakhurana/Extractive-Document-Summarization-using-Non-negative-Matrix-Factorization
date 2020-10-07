<h1>Extractive Document Summarization using Non-negative Matrix Factorization</h1>

This repository contains Python (v 3.6) scripts for implementation of NMF-TR and NMF-TP methods for Single document extractive summarization.
<br/>
**NMF-TR**: Term-oriented Extractive Summarization
<br/>
**NMF-TP**: Topic-oriented Extractive Summarization

<br/>
**Author**:  Alka Khurana
**Acknowledgement**: Vasudha Bhatnagar
<br/>
**Description:**
Both the algorithms generate score for each sentence (TR-score, TP-score) in the input document and present the sentences in the descending order of their scores.
Top scoring sentences are included in the document summary until required summary length is complete. 
<br/>
# Citation:
<br/>
```
@inproceedings{khurana2019extractive,
  title={Extractive Document Summarization using Non-negative Matrix Factorization},
  author={Khurana, Alka and Bhatnagar, Vasudha},
  booktitle={International Conference on Database and Expert Systems Applications},
  pages={76--90},
  year={2019},
  organization={Springer}
}
```
**Pipeline:**
1. Clone the complete directory.
2. Put the documents in the Documents folder for which summary is to be generated.
3. In all the .py files, change the current directory to working directory of your system.
4. Run Preprocessing.py for pre-processing the input documents.
5. Run NNDSVD_TR.py  for generating the summary of the text using Term-oriented method. Run NNDSVD_TP.py  for generating the summary of the text using Topic-oriented method.

