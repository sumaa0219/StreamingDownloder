import requests
import m3u8
import ffmpeg

playlist = m3u8.load("cam6_v1_video_1080P_.m3u8")
BaseURL = "https://vod.spwn.jp/spwn-vod/23031801-jphololive4thfes/grp1/cam6_v1/"

for i, segment in enumerate(playlist.segments):
    # tsファイルのパス
    uri = segment.absolute_uri
    URL = BaseURL + uri
    print(URL)
    # ffmpeg.input(URL).output(f'video/{uri}').run()
    stream = ffmpeg.input(URL)
    stream = ffmpeg.output(stream, "video/"+uri)
    ffmpeg.run(stream)
