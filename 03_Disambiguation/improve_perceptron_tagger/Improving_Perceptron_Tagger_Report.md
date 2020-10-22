mproving Perceptron Tagger:

The evaluation result on the test data gave a score of 96.29 UPOS.

Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
UPOS       |     96.29 |     96.29 |     96.29 |     96.29

The evaluation result on the dev data gave a score of 96.57 UPOS.

Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
UPOS       |     96.57 |     96.57 |     96.57 |     96.57

To improve this score, I tried to make various modifications in the _get_features() in tagger.py, some of which are: 

add('i-1 word+i+1word', context[i-1], context[i+1])
add('bias_2')
add('i-2 suffix', context[i-2][-3:])
add('i+2 suffix', context[i+2][-3:])

I could not increase the score. Some changes made caused the score to decrease, which I have not included in the report. At the end of this experiment, the score remains to be 96.57

