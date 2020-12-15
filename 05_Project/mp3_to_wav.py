import os
from pydub import AudioSegment

# path = "input_audio/Punjabi"
# path = "input_audio/Assamese"
# path = "input_audio/Odiya"
path = "input_audio/Tamil"

AudioSegment.converter = "D:/Deeps/Fall20/ComputationalLinguisticAnalysis/Project/ffmpeg-4.3.1-win64-static/bin/ffmpeg.exe"
AudioSegment.ffmpeg = "D:/Deeps/Fall20/ComputationalLinguisticAnalysis/Project/ffmpeg-4.3.1-win64-static/bin/ffmpeg.exe"
AudioSegment.ffprobe ="D:/Deeps/Fall20/ComputationalLinguisticAnalysis/Project/ffmpeg-4.3.1-win64-static/bin/ffprobe.exe"

#Change working directory
os.chdir(path)

audio_files = os.listdir()

for file in audio_files:

    name, ext = os.path.splitext(file)
    if ext == ".mp3":
       mp3_sound = AudioSegment.from_mp3(file)
       mp3_sound.export("{0}.wav".format(name), format="wav")