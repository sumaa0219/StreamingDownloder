import requests

# cookie = { #day2
#     'CloudFront-Key-Pair-Id': 'K33HSRY3XILYEV',
#     'CloudFront-Policy': 'eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly92b2QyLnNwd24uanAvc3B3bi12b2QyLzIzMDMxODAxLWpwaG9sb2xpdmU0dGhmZXMvZ3JwMS9jYW02X3YxLyoiLCJDb25kaXRpb24iOnsiSXBBZGRyZXNzIjp7IkFXUzpTb3VyY2VJcCI6IjAuMC4wLjAvMCJ9LCJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY4MjA4OTE5OTAwMH19fV19',
#     'CloudFront-Signature': 'DSrlrggTvOzNDRXWKZnb6c-68ljxk+gDcGVvzI5LGyeSXoA6gI7tps5nGnS1Oa1Loo~3Kcq02nBUsyIfVdEAaGVAo2p+BYs3PQE5JrYmiewMDFm395qSs8+z8hqOFg9r3uAY3T9GQgZA9En2FmQDMDSaf/r+5xDQqwNynOm+swxqVl7g7FrF1BrXGW0pdn8Dowv9Sh3+Fzu00roYOyXoq6vESWwk5t27v8a9zw7B6sT2TFkOW3BlMFVq4DXVwwYNVUVrQELU0cQGAPH2QzernG78g88m026X7y5WnkfKvDYTb2upuokNw8/BNq7eH73uGMbDQdLg3EV2zov4QCHnEA_'
# }


# cookie = { #day1
#     "CloudFront-Key-Pair-Id":"K33HSRY3XILYEV",
#     "uid":"xKe6liSAJ5QZOo1T99GDffBjnhD2",
#     "last-domain":"virtual.spwn.jp",
#     "CloudFront-Policy":"eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly92b2QyLnNwd24uanAvc3B3bi12b2QyLzIzMDMxODAxLWpwaG9sb2xpdmU0dGhmZXMvZ3JwMi9jYW0xX3YxLyoiLCJDb25kaXRpb24iOnsiSXBBZGRyZXNzIjp7IkFXUzpTb3VyY2VJcCI6IjAuMC4wLjAvMCJ9LCJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY4MjA4OTE5OTAwMH19fV19",
#     "CloudFront-Signature":"T0rQYTgWYa6nPTE6OPOCqeFF2jxailNi6fRZ9MytLeYX5c7jz3vGebuNyoZie9UPtDuhIN9aqhhYEzVffk3slIwSJ1awNslNWgrqhB5OpVYyt9vCHUfy1aslF3F3FnRI9pwxhCgNH6~7HLQRhy6H3HGcr3JgnsRAMFZKYIXXwTPfVL1T7hC045YnVbwxvRYjP7pHWUJt/jQYccxvFZHG/v1d3KakawSv3QiiZoBK34NLNpI1JKTWfqcFobQJV8joHXKdfaxipttoHCZQb4kexlmMeaQLJFqMKHEoN3fOMk4ATq7ZemSfzyV-rozjhYTgrs7Ru6tKuuhDTR5LRxVjew_="
# }

# cookie = { #holo*27
#     "CloudFront-Key-Pair-Id" :"K33HSRY3XILYEV",
#     "CloudFront-Policy":"eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly92b2Quc3B3bi5qcC9zcHduLXZvZC8yMzAzMTgwMS1qcGhvbG9saXZlNHRoZmVzL2dycDEvY2FtNV92MS8qIiwiQ29uZGl0aW9uIjp7IklwQWRkcmVzcyI6eyJBV1M6U291cmNlSXAiOiIwLjAuMC4wLzAifSwiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2ODIwODkxOTkwMDB9fX1dfQ=",
#     "CloudFront-Signature":"fWE2NP4y2jwvdwAsW0cVnNnfL6ftvwu05EucIlITi~Ta7KZkJqiCdL4uqqEiV2Hke/h4DXLds71PjRuh6UT8IJZ8omepB5rflQ6xA1qbCpRlR9KPjbmqQAQTcuFrHl3cL/5aRqptG85N4Upx5/c605OOze8IYo6ejp7NfosM9hGZ-OUxwdUpKtQivWK3pjLopteFbs0toLfUsprrMzwAuiVEOhD7zw46mRkiW6pkjXu3GVvHr4pwoyV7HLVNR5+bE3hCp8j4VNjyCGZ7BbhX2mIDUIJTASvg3Tq1r17jXphSrdjt/3ZvugcJMzowQvyZG1ydapfpCBtIdggn1I+iug="
# }

cookie = {
    "_ga": "GA1.2.515259547.1693205423",
    "_gid": "GA1.2.1905885617.1693205423",
    "Z-aN_sid": "s%3A5Le7VuWX5HODAss2bJrH1kSNbmc2Pbp7.pm2w%2BjOoaTRTx%2BvtRaJtgLZ1AJmu02AoombqVyas%2FeQ",
    "hdnts": "st%3D1693205530~exp%3D1693206070~acl%3D%2Fout%2Fv1%2F68f3b43a30cd4c36b2d1fbbd5ce7683c%2F*~hmac%3Df6fc1218737bd2cabf87157b4f2f005133cea57cf295dc1e6a2be76cba8e6a67",
    "Z-aN-uat": "1693291930.138472.gZZUl1A-j_XQRpoFiqdYfdOo.5785d7e04cb8134589e51c1500cdb15fb47d241ed7824a23a9cbd28417eab944"
}

r = requests.get(
    'https://vodarc01-ca-02.zan-live.com/ySMKIw2UeB2X7SpwHSpwDw_1424/index_1/00000/index_1_02497.ts', cookies=cookie)

print(r)
