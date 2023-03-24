import requests
import m3u8
import ffmpeg
import webbrowser
import time

playlist = m3u8.load("cam6_v1_video_1080P_.m3u8")
BaseURL = "https://vod2.spwn.jp/spwn-vod2/23031801-jphololive4thfes/grp1/cam6_v1/"

cookie = {
    '_gcl_au': '1.1.2035114548.1679276547',
    '_ga': 'GA1.2.1698492336.1679276547',
    'CloudFront-Key-Pair-Id': 'K33HSRY3XILYEV',
    'CloudFront-Policy': 'eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly92b2QyLnNwd24uanAvc3B3bi12b2QyLzIzMDMxODAxLWpwaG9sb2xpdmU0dGhmZXMvZ3JwMS9jYW02X3YxLyoiLCJDb25kaXRpb24iOnsiSXBBZGRyZXNzIjp7IkFXUzpTb3VyY2VJcCI6IjAuMC4wLjAvMCJ9LCJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY4MjA4OTE5OTAwMH19fV19',
    'CloudFront-Signature': 'DSrlrggTvOzNDRXWKZnb6c-68ljxk+gDcGVvzI5LGyeSXoA6gI7tps5nGnS1Oa1Loo~3Kcq02nBUsyIfVdEAaGVAo2p+BYs3PQE5JrYmiewMDFm395qSs8+z8hqOFg9r3uAY3T9GQgZA9En2FmQDMDSaf/r+5xDQqwNynOm+swxqVl7g7FrF1BrXGW0pdn8Dowv9Sh3+Fzu00roYOyXoq6vESWwk5t27v8a9zw7B6sT2TFkOW3BlMFVq4DXVwwYNVUVrQELU0cQGAPH2QzernG78g88m026X7y5WnkfKvDYTb2upuokNw8/BNq7eH73uGMbDQdLg3EV2zov4QCHnEA_'
}

for i, segment in enumerate(playlist.segments):
    # tsファイルのパス
    uri = segment.absolute_uri
    URL = BaseURL + uri
    print(URL)
    r = requests.get(url=URL, cookies=cookie)
    with open(f'video/{uri}', 'wb') as saveFile:

        saveFile.write(r.content)


videos = []

for i, segment in enumerate(playlist.segments):
    videos.append("video/" + segment.absolute_uri)

# videos = ["ts/1.ts", "ts/2.ts", "ts/3.ts", "ts/4.ts", "ts/5.ts"]  # 結合するファイルのパス
# 一旦テキストファイルに書き出す
# 書き出さない方法は、あまりにファイル数が多い場合に「コマンド長すぎ」と怒られる
with open("tmp.txt", "w") as fp:
    lines = [f"file '{line}'" for line in videos] # file 'パス' という形式にする
    fp.write("\n".join(lines))
# ffmpegで結合（再エンコードなし）
ffmpeg.input("tmp.txt", f="concat", safe=0).output("out.mp4", c="copy").run()
