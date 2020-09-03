Exercises with Sort

Folding case : sed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | sort | uniq -c | sort -f
Rhyming order : sed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | sort | rev | uniq -c | sort -nr 

Exercises with grep:

* Upper case words: 127490

    sed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | grep -c '^[A-Z]'

* Lower case words: 273397

    sed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | grep -c '^[a-z]'

* 4-Letter words: 72783

    sed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | grep -c '^[A-Za-z][A-Za-z][A-Za-z][A-Za-z]$'

* No vowel words: 9303

    sed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | grep -i -E -c '^[^aeiou]+$'

* One syllabal words: 120501

    sed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | grep -i -E -c '^[^aeiou] *[aeiou][^aeiou]*$'

* Two syllabal words: 71903

    sed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | grep -i -E -c '^[^aeiou] *[aeiou][^aeiou] *[aeiou][^aeiou]$'


Exercises with sed:

* Initial consonant sequences: 
    Run shell file:  bash initial-consonants.sh < wiki.txt > initial-consonants.hist  
    Ouput written to file: initial-consonants.hist

* Final consonant sequences
    Run shell file:  bash final-consonants.sh < wiki.txt > final-consonants.hist  
    Ouput written to file: final-consonants.hist

