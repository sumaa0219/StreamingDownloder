import ffmpeg

video = "out.mp4"
audio = "out27.aac"

ffmpeg_video = ffmpeg.input(video)
ffmpeg_audio = ffmpeg.input(audio)

stream = ffmpeg.output(ffmpeg_video, ffmpeg_audio,
                       "Hololive-4fes-Our-Bright-Parade.mp4", vcodec="copy", acodec="aac")
ffmpeg.run(stream)
