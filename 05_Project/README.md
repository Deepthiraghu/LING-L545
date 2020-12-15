# Project

This project involves identification of the language from uncommon Indian languages - Tamil, Odiya, Punjabi and Assamese. The idea is to first translate the audio data into text using DeepSpeech, an open source speech recognizer. As the next step, the recognized text is fed into a character based n-gram model to identify the corresponding language. Uncommon Indian languages from https://commonvoice.mozilla.org/en/languages is used as the datasets to train the language identification model. This project will be useful to tag uncommon languages spoken in YouTube videos. Tagging these uncommon languages will help in expanding the number of languages for which subtitles can be submitted on YouTube.

# File Description

* `mp3_to_wav.py ` converts the audio file format from mp3 to wav.

* `deepspeech_transcribe.py` reads the wav audio files and transcribes it into English text. It produces the four text files `input_assamese.txt`, `input_odiya.txt`, `input_punjabi.txt`, `input_tamil.txt`, which are used as training data and the four text files `test_assamese.txt`, `test_odiya.txt`, `test_punjabi.txt`, `test_tamil.txt`, which are used as test data.

* `Language_Identifier.ipynb` is the python notebook which consists of the n-gram model which has been trained to identify the language. This notebook consists of data preprocessing steps, the training, testing and accuracy calculation code.

* `Final_Project_Paper.pdf` is the ACL style paper describing this project.