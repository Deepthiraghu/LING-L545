# Report

I worked with the Finnish dataset. Below are the evaluation results:

```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |    100.00 |    100.00 |    100.00 |    100.00
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |    100.00 |    100.00 |    100.00 |    100.00
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |     84.58 |     84.58 |     84.58 |     84.58
LAS        |     81.93 |     81.93 |     81.93 |     81.93

```

## Errors
### On comparing the tree, the error made by the parser is that when a sentence is long, it connects nouns or verbs to a previously encountered verb

#### Example:

sent_id = b104.3

text = Varasin pupulle ja minulle sekä sille sisarentyttärelleni, joka pääsi Turkuun lakia lukemaan, liput kaupunginteatterin Laulavat sadepisarat -musikaaliin.

In this sentence, the below differences are seen:

```
minulle - pronoun
    Expected: dependent on pupulle Noun 
    Test: dependent on Varasin Verb
    Label: conj

sisarentyttärelleni - Noun
    Expected: dependent on pupulle Noun 
    Test: dependent on Varasin Verb
    Label: conj

pääsi - Verb
    Expected: dependent on sisarentyttärelleni Noun
    Test: dependent on Varasin Verb
    Label: acl:relcl

kaupunginteatterin - Noun
    Expected: dependent on -musikaaliin Noun with nmod:poss
    Test: dependent on Laulavat verb with nsubj

sadepisarat - Noun
    Expected: dependent on -musikaaliin Noun with compound:nn
    Test: dependent on lukemaan Verb with obj

-musikaaliin - Noun
    Expected: dependent on liput Noun with nmod
    Test: dependent on lukemaan Verb with obj
```
