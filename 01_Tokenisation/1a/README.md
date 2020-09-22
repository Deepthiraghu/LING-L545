## Sentence Segmentation

I used the corpus in one of the article bundles of enwiki, [enwiki-20200901-pages-articles2.xml-p30304p88444.bz2](https://dumps.wikimedia.org/enwiki/20200901/enwiki-20200901-pages-articles2.xml-p30304p88444.bz2) (213.6 MB). 
Pragmatic segmenter is a rule-based segmenter, and Punkt is a stat-based segmenter. In the article that I have chosen, Pragmatic segmenter has 2444428 sentences and Punkt segmenter has 2503172 sentences. I have saved the first 50 sentences in each file for comparison.

To see the difference between the two segmentation methods, I compared the two outputs ([pragmatic_segmenter.txt](1a/segmentation/pragmatic_segmenter.txt) and [punkt.txt](1a/segmentation/punkt.txt)) with the command  `diff -y -W 120 pragmatic_segmenter.txt punkt.txt`.

### Pragmatic Segmenter

Pragmatic Segmenter seems to work well on sentences with quotes, even if the sentence is long and has nested quotes. 

In some cases, pragmatic segmenter did not segment the sentence correctly. Below is an example sentence:

According to a later description by McLaren, "When Sid joined he couldn't play guitar but his craziness fit into the structure of the band. He was the knight in shining armour with a giant fist." "Everyone agreed he had the look," Lydon later recalled, but musical skill was another matter.

This sentence should have been split into:

Sentence 1: According to a later description by McLaren, "When Sid joined he couldn't play guitar but his craziness fit into the structure of the band. He was the knight in shining armour with a giant fist." 

Sentence 2: "Everyone agreed he had the look," Lydon later recalled, but musical skill was another matter.

But pragmatic segmenter considered this as a single sentence. 


Another example:

"The X-Files" Collectible Card Game was released in 1996 and an expansion set was released in 1997. 

This should have been a single sentence, but pragmatic segmenter segments it into two sentences:

Sentence 1: "The X-Files"

Sentence 2: Collectible Card Game was released in 1996 and an expansion set was released in 1997. 

Apart from such few overlooks, pragmatic segmenter works well, with an accuracy of 98.08%

### NLTK’s Punkt

The difference in sentences between Punkt and Pragmatic segmenter is 58744. Punkt recognizes many sentences incorrectly, which pragmatic segmenter got right.

Sentences with numbers, nested quotes, sentences within quotes, abbreviations with punctuations (like B.S., e.g., i.e) were segmented incorrectly by Punkt.

Example:

Sentence 1: The trio was introduced in the first-season episode "E.B.E." as a way to make Mulder appear more credible.

This sentence is split incorrectly because of the abbreviation E.B.E. (Punkt splits this into two sentences, but it should've been one single sentence)

Sentence 2: The resulting riff pleased Carter; Snow said, "this sound was in the keyboard. And that was it."

This sentence is split incorrectly because of sentences within quotes (Punkt splits this into two sentences, but it should've been one single sentence)

Assuming all the differences in sentences is due to Punkt's wrong segmentation, it's accuracy is about 97%.


## Tokenization

My implementation of the Max Match Algorithm is in the file [max_match_algo.py](1a/tokenizer/max_match_algo.py). The program can be executed as:

```
python3 max_match_algo.py < ja_gsd-ud-train.conllu > max_match_output.txt 
```

The output is stored in [max_match_output.txt](1a/tokenizer/max_match_output.txt)

### Word Error Rate:

The program to calculate WER can be found in the file [word_error_rate.py](1a/tokenizer/word_error_rate.py). The program can be executed as:
The word error rate was calculated by the below command:

```
python3 word_error_rate.py reference.txt hypothesis.txt > word_error_rate.txt 
```

The WER results ar stored in [word_error_rate.txt](1a/tokenizer/word_error_rate.txt). The results obtained are somewhere between 25% to 28%.
