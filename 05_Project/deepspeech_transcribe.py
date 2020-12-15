from deepspeech import Model
import scipy.io.wavfile as wav
import sys
import os as os

ds = Model('deepspeech-0.9.1-models.pbmm')

pathToAudio = sys.argv[1]
language = sys.argv[2]
audio_files = os.listdir(pathToAudio)
for eachfile in audio_files :
    if eachfile.endswith(".wav"):
        file_Path = pathToAudio + eachfile
        print("File to be read is ",  file_Path)    
        fs, audio = wav.read(file_Path)
        processed_data = ds.stt(audio)
        print("Processed Data : " , processed_data)
        with open("input_"+language+".txt", 'a') as f:
            f.write(processed_data+"\n")