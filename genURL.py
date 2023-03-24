import requests
import m3u8
import ffmpeg
import webbrowser

playlist = m3u8.load("cam6_v1_audio_320kbps_48k_.m3u8")
BaseURL = "https://vod2.spwn.jp/spwn-vod2/23031801-jphololive4thfes/grp1/cam6_v1/"

# cookie = {
#     "_gcl_au": "1.1.1036691919.1679496523",
#     "CloudFront-Key-Pair-Id": "K33HSRY3XILYEV",
#     "CloudFront-Policy": "eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly92b2QyLnNwd24uanAvc3B3bi12b2QyLzIzMDMxODAxLWpwaG9sb2xpdmU0dGhmZXMvZ3JwMS9jYW02X3YxLyoiLCJDb25kaXRpb24iOnsiSXBBZGRyZXNzIjp7IkFXUzpTb3VyY2VJcCI6IjAuMC4wLjAvMCJ9LCJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY4MjA4OTE5OTAwMH19fV19",
#     "CloudFront-Signature" :"DSrlrggTvOzNDRXWKZnb6c-68ljxk+gDcGVvzI5LGyeSXoA6gI7tps5nGnS1Oa1Loo~3Kcq02nBUsyIfVdEAaGVAo2p+BYs3PQE5JrYmiewMDFm395qSs8+z8hqOFg9r3uAY3T9GQgZA9En2FmQDMDSaf/r+5xDQqwNynOm+swxqVl7g7FrF1BrXGW0pdn8Dowv9Sh3+Fzu00roYOyXoq6vESWwk5t27v8a9zw7B6sT2TFkOW3BlMFVq4DXVwwYNVUVrQELU0cQGAPH2QzernG78g88m026X7y5WnkfKvDYTb2upuokNw8/BNq7eH73uGMbDQdLg3EV2zov4QCHnEA_=",
# }
# header = {
#     # ":path": "/spwn-vod2/23031801-jphololive4thfes/grp1/cam6_v1/cam6_v1_video_1080P_20230320T131916_00001.ts",
#     # ":scheme": "https",
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7",
#     "cache-control": "no-cache",
#     "cookie": "_gcl_au=1.1.1036691919.1679496523; CloudFront-Key-Pair-Id=K33HSRY3XILYEV; CloudFront-Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly92b2QyLnNwd24uanAvc3B3bi12b2QyLzIzMDMxODAxLWpwaG9sb2xpdmU0dGhmZXMvZ3JwMS9jYW02X3YxLyoiLCJDb25kaXRpb24iOnsiSXBBZGRyZXNzIjp7IkFXUzpTb3VyY2VJcCI6IjAuMC4wLjAvMCJ9LCJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY4MjA4OTE5OTAwMH19fV19; CloudFront-Signature=DSrlrggTvOzNDRXWKZnb6c-68ljxk+gDcGVvzI5LGyeSXoA6gI7tps5nGnS1Oa1Loo~3Kcq02nBUsyIfVdEAaGVAo2p+BYs3PQE5JrYmiewMDFm395qSs8+z8hqOFg9r3uAY3T9GQgZA9En2FmQDMDSaf/r+5xDQqwNynOm+swxqVl7g7FrF1BrXGW0pdn8Dowv9Sh3+Fzu00roYOyXoq6vESWwk5t27v8a9zw7B6sT2TFkOW3BlMFVq4DXVwwYNVUVrQELU0cQGAPH2QzernG78g88m026X7y5WnkfKvDYTb2upuokNw8/BNq7eH73uGMbDQdLg3EV2zov4QCHnEA_=",
#     "pragma": "no-cache",
#     "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"macOS"',
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "none",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": "1",
#     }
for i, segment in enumerate(playlist.segments):
    # tsファイルのパス
    uri = segment.absolute_uri
    URL = BaseURL + uri
    print(URL)
    # ffmpeg.input(URL).output(f'video/{uri}').run()
    # stream = ffmpeg.input(URL,headers=f'Cookie:{cookie}\r\n')
    # stream = ffmpeg.output(stream, f'./video/{uri}')
    # ffmpeg.run(stream)
# URL = "https://vod2.spwn.jp/spwn-vod2/23031801-jphololive4thfes/grp1/cam6_v1/cam6_v1_video_1080P_20230320T131916_00001.ts"
    
    webbrowser.open(URL)

