from tqdm import tqdm
import ffmpeg
import m3u8

# playlist = m3u8.load("cam6_v1_audio_320kbps_48k_.m3u8") #day2
# audio_playlist = m3u8.load("index_7.m3u8") #day1
audio_playlist = m3u8.load("cam5_v1_audio_320kbps_48k_.m3u8") #holo*27
videos = []

for i, segment in enumerate(audio_playlist.segments):
    videos.append("audio/" + segment.absolute_uri)

# videos = ["ts/1.ts", "ts/2.ts", "ts/3.ts", "ts/4.ts", "ts/5.ts"]  # 結合するファイルのパス
# 一旦テキストファイルに書き出す
# 書き出さない方法は、あまりにファイル数が多い場合に「コマンド長すぎ」と怒られる
with open("tmp.txt", "w") as fp:
    lines = [f"file '{line}'" for line in videos] # file 'パス' という形式にする
    fp.write("\n".join(lines))
# ffmpegで結合（再エンコードなし）
ffmpeg.input("tmp.txt", f="concat", safe=0).output("out27.aac", c="copy").run()