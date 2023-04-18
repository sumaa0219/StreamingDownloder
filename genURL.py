import requests
import m3u8
import ffmpeg
import webbrowser
import time

# audio_playlist = m3u8.load("index_7.m3u8") #day1
# video_playlist = m3u8.load("index_12.m3u8") #day1
# audio_playlist = m3u8.load("cam6_v1_audio_320kbps_48k_.m3u8") #day2
# video_playlist = m3u8.load("cam6_v1_audio_320kbps_48k_.m3u8") #day2
audio_playlist = m3u8.load("cam5_v1_audio_320kbps_48k_.m3u8") #Holo*27
video_playlist = m3u8.load("cam5_v1_video_1080P_.m3u8") #Holo*27

# BaseURL = "https://vod2.spwn.jp/spwn-vod2/23031801-jphololive4thfes/grp2/cam1_v1/" #day1
# BaseURL = "https://vod2.spwn.jp/spwn-vod2/23031801-jphololive4thfes/grp1/cam6_v1/" #day2
BaseURL = "https://vod.spwn.jp/spwn-vod/23031801-jphololive4thfes/grp1/cam5_v1/" #holo27


cookie_day2 = {
    '_gcl_au': '1.1.2035114548.1679276547',
    '_ga': 'GA1.2.1698492336.1679276547',
    'CloudFront-Key-Pair-Id': 'K33HSRY3XILYEV',
    'CloudFront-Policy': 'eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly92b2QyLnNwd24uanAvc3B3bi12b2QyLzIzMDMxODAxLWpwaG9sb2xpdmU0dGhmZXMvZ3JwMS9jYW02X3YxLyoiLCJDb25kaXRpb24iOnsiSXBBZGRyZXNzIjp7IkFXUzpTb3VyY2VJcCI6IjAuMC4wLjAvMCJ9LCJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY4MjA4OTE5OTAwMH19fV19',
    'CloudFront-Signature': 'DSrlrggTvOzNDRXWKZnb6c-68ljxk+gDcGVvzI5LGyeSXoA6gI7tps5nGnS1Oa1Loo~3Kcq02nBUsyIfVdEAaGVAo2p+BYs3PQE5JrYmiewMDFm395qSs8+z8hqOFg9r3uAY3T9GQgZA9En2FmQDMDSaf/r+5xDQqwNynOm+swxqVl7g7FrF1BrXGW0pdn8Dowv9Sh3+Fzu00roYOyXoq6vESWwk5t27v8a9zw7B6sT2TFkOW3BlMFVq4DXVwwYNVUVrQELU0cQGAPH2QzernG78g88m026X7y5WnkfKvDYTb2upuokNw8/BNq7eH73uGMbDQdLg3EV2zov4QCHnEA_'
}

cookie_day1 = {
    "CloudFront-Key-Pair-Id":"K33HSRY3XILYEV",
    "uid":"xKe6liSAJ5QZOo1T99GDffBjnhD2",
    "last-domain":"virtual.spwn.jp",
    "CloudFront-Policy":"eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly92b2QyLnNwd24uanAvc3B3bi12b2QyLzIzMDMxODAxLWpwaG9sb2xpdmU0dGhmZXMvZ3JwMi9jYW0xX3YxLyoiLCJDb25kaXRpb24iOnsiSXBBZGRyZXNzIjp7IkFXUzpTb3VyY2VJcCI6IjAuMC4wLjAvMCJ9LCJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY4MjA4OTE5OTAwMH19fV19",
    "CloudFront-Signature":"T0rQYTgWYa6nPTE6OPOCqeFF2jxailNi6fRZ9MytLeYX5c7jz3vGebuNyoZie9UPtDuhIN9aqhhYEzVffk3slIwSJ1awNslNWgrqhB5OpVYyt9vCHUfy1aslF3F3FnRI9pwxhCgNH6~7HLQRhy6H3HGcr3JgnsRAMFZKYIXXwTPfVL1T7hC045YnVbwxvRYjP7pHWUJt/jQYccxvFZHG/v1d3KakawSv3QiiZoBK34NLNpI1JKTWfqcFobQJV8joHXKdfaxipttoHCZQb4kexlmMeaQLJFqMKHEoN3fOMk4ATq7ZemSfzyV-rozjhYTgrs7Ru6tKuuhDTR5LRxVjew_="
}

cookie_holo27 = { #holo*27
    "CloudFront-Key-Pair-Id" :"K33HSRY3XILYEV",
    "CloudFront-Policy":"eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly92b2Quc3B3bi5qcC9zcHduLXZvZC8yMzAzMTgwMS1qcGhvbG9saXZlNHRoZmVzL2dycDEvY2FtNV92MS8qIiwiQ29uZGl0aW9uIjp7IklwQWRkcmVzcyI6eyJBV1M6U291cmNlSXAiOiIwLjAuMC4wLzAifSwiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2ODIwODkxOTkwMDB9fX1dfQ=",
    "CloudFront-Signature":"fWE2NP4y2jwvdwAsW0cVnNnfL6ftvwu05EucIlITi~Ta7KZkJqiCdL4uqqEiV2Hke/h4DXLds71PjRuh6UT8IJZ8omepB5rflQ6xA1qbCpRlR9KPjbmqQAQTcuFrHl3cL/5aRqptG85N4Upx5/c605OOze8IYo6ejp7NfosM9hGZ-OUxwdUpKtQivWK3pjLopteFbs0toLfUsprrMzwAuiVEOhD7zw46mRkiW6pkjXu3GVvHr4pwoyV7HLVNR5+bE3hCp8j4VNjyCGZ7BbhX2mIDUIJTASvg3Tq1r17jXphSrdjt/3ZvugcJMzowQvyZG1ydapfpCBtIdggn1I+iug="
}

# for i, segment in enumerate(audio_playlist.segments):
#     # tsファイルのパス
#     uri = segment.absolute_uri
#     URL = BaseURL + uri
#     print(URL)
#     r = requests.get(url=URL, cookies=cookie_holo27)
#     with open(f'audio/{uri}', 'wb') as saveFile:

#         saveFile.write(r.content)

for i, segment in enumerate(video_playlist.segments):
    # tsファイルのパス
    uri = segment.absolute_uri
    URL = BaseURL + uri
    print(URL)
    r = requests.get(url=URL, cookies=cookie_holo27)
    with open(f'video/{uri}', 'wb') as saveFile:

        saveFile.write(r.content)

