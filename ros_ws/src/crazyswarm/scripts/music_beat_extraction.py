import librosa

y, sr = librosa.load('perfect.mp3')

tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
time_stamps = librosa.frames_to_time(beats, sr=sr)
print(time_stamps)