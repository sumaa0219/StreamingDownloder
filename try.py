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

cookie = { #holo*27
    "CloudFront-Key-Pair-Id" :"K33HSRY3XILYEV",
    "CloudFront-Policy":"eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly92b2Quc3B3bi5qcC9zcHduLXZvZC8yMzAzMTgwMS1qcGhvbG9saXZlNHRoZmVzL2dycDEvY2FtNV92MS8qIiwiQ29uZGl0aW9uIjp7IklwQWRkcmVzcyI6eyJBV1M6U291cmNlSXAiOiIwLjAuMC4wLzAifSwiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2ODIwODkxOTkwMDB9fX1dfQ=",
    "CloudFront-Signature":"fWE2NP4y2jwvdwAsW0cVnNnfL6ftvwu05EucIlITi~Ta7KZkJqiCdL4uqqEiV2Hke/h4DXLds71PjRuh6UT8IJZ8omepB5rflQ6xA1qbCpRlR9KPjbmqQAQTcuFrHl3cL/5aRqptG85N4Upx5/c605OOze8IYo6ejp7NfosM9hGZ-OUxwdUpKtQivWK3pjLopteFbs0toLfUsprrMzwAuiVEOhD7zw46mRkiW6pkjXu3GVvHr4pwoyV7HLVNR5+bE3hCp8j4VNjyCGZ7BbhX2mIDUIJTASvg3Tq1r17jXphSrdjt/3ZvugcJMzowQvyZG1ydapfpCBtIdggn1I+iug="
}


r = requests.get('https://vod.spwn.jp/spwn-vod/23031801-jphololive4thfes/grp1/cam5_v1/cam5_v1_audio_320kbps_48k_20230320T044807_00001.aac', cookies=cookie)

print(r)
