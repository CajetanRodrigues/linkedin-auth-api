import requests
import webbrowser

params = dict(response_type='code', client_id='8641437gs2tceu',state='state',scope='r_liteprofile%20r_emailaddress%20w_member_social')

res = requests.post('https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&code=AQQ6ncSEQHJH9PnMfh5VsYyUqw5wxgZlXpK1UHI5yT8XVQfn81XIa6DnSmmKDQADfCaHPcy1EZZkxDZ9mv2SJfWrXPmfxhRXI4PDbEGmD6hkTPgCyqcv0KvLxA62_QJ3kzsXB1E6R3BjeOfXwTAgO6grPv5d5gO7LrEMf30IOemNTw_JRog3-XSbc1hqQw&scope=r_liteprofile%20r_emailaddress%20w_member_social&redirect_uri=http://localhost:4200/profile/&client_secret=PNWIlG7Tgjo0MBBh&client_id=81u411hl9z91tg')
# webbrowser.open('https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&code=AQRNY_A5ICGjOdzCfeyyK6jlEpby1U7OMiFbdwma2g9wWAHIyurLR-otf3cdPBvPMI9xAAk19-jZ85rQ6ytoC6RTwVeo-yu3fuMrislAjVuo7MZnCUX_iaeHxeHfsOB4_jDJNCl84-ECYaSNkFxLFm12u94UOkDMBiFJVYpoSt3JuhRH8E__BRv1UdASrw&scope=r_liteprofile%20r_emailaddress%20w_member_social&redirect_uri=http://localhost:4200/profile&client_secret=PNWIlG7Tgjo0MBBh&client_id=8641437gs2tceu')
print(res.text)