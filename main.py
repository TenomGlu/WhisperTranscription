import subprocess
import whisper_timestamped as whisper

consentVideo = 'Consent .mp4'
ConsentTranscript = 'consent_transcript.txt'

ContraceptionVideo = 'Contraception.mp4'
ContraceptionTranscript = 'contraception_transcript.txt'

currentVideo = consentVideo
currentTranscript = ConsentTranscript

model = whisper.load_model("base")

video_in = currentVideo
audio_out = currentVideo

ffmpeg_cmd = f"ffmpeg -i {video_in} -vn -c:a libmp3lame -b:a 192k {audio_out}"

subprocess.run(["ffmpeg", "-i", video_in, "-vn", "-c:a", "libmp3lame", "-b:a", "192k", audio_out])

result = model.transcribe(audio_out)
newDict = {}
with open(currentTranscript, 'w') as f:
    iterator = 0
    while iterator < len(result['segments']):
        lineInMemory = (result['segments'][iterator])
        if lineInMemory['start'] > 60:
            minutes = int(lineInMemory['start']/60)
            seconds = int(lineInMemory['start'] % 60)
            if seconds < 10:
                seconds = "0" + str(seconds)
            f.write("(" + str(minutes) + ":" + str(seconds) + "s" + ")" + ":")
            f.write(lineInMemory['text'])
            f.write("\n")
        else:
            minutes = int(lineInMemory['start'] / 60)
            seconds = int(lineInMemory['start'] % 60)
            if seconds < 10:
                seconds = "0" + str(seconds)
            f.write("(" + str(minutes) + ":" + str(seconds) + "s" + ")" + ":")
            f.write(lineInMemory['text'])
            f.write("\n")
        iterator += 1

f.close()
