import subprocess
import whisper_timestamped as whisper
from pathlib import Path

# Creating a variable that references the path of the mp4 being transcribed
video_location = 'Consent .mp4'

# Creating a variable that references the path of the mp3 converted file
video_transcriptions = 'transcriptaudio.mp3'

# Load the whisper model
model = whisper.load_model("base")

video_in = video_location
audio_out = video_location

ffmpeg_cmd = f"ffmpeg -i {video_in} -vn -c:a libmp3lame -b:a 192k {audio_out}"

subprocess.run(["ffmpeg", "-i", video_in, "-vn", "-c:a", "libmp3lame", "-b:a", "192k", audio_out])

result = model.transcribe(audio_out)

# Write to a text file
with open('transcript.txt', 'w') as f:
    f.write(str(result))
f.close()

# Still need to add parsing feature so that transcription can be copy-pasted into a text file in a neat format only one time with only
# minor changes necessary
