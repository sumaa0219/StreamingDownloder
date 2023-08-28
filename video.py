import requests
import m3u8
import ffmpeg
import os
import webbrowser
import time

# playlist = m3u8.load("cam6_v1_video_1080P_.m3u8")
playlist = m3u8.load("index_1.m3u8")
# playlist = m3u8.load("index_12.m3u8")


videos = []

for i, segment in enumerate(playlist.segments):
    videos.append(os.path.join("video", segment.absolute_uri))


# videos = ["ts/1.ts", "ts/2.ts", "ts/3.ts", "ts/4.ts", "ts/5.ts"]  # 結合するファイルのパス
# 一旦テキストファイルに書き出す
# 書き出さない方法は、あまりにファイル数が多い場合に「コマンド長すぎ」と怒られる
with open("tmp.txt", "w") as fp:
    lines = [f"file '{line}'" for line in videos]  # file 'パス' という形式にする
    fp.write("\n".join(lines))
# ffmpegで結合（再エンコードなし）
ffmpeg.input("tmp.txt", f="concat", safe=0).output("out.mp4", c="copy").run()
