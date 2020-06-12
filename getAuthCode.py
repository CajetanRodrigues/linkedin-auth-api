import requests
import webbrowser

params = dict(response_type='code', client_id='8641437gs2tceu',state='DCEeFWf45A53sdfKef424s',scope='r_liteprofile%20r_emailaddress%20w_member_social')

# res = requests.get('https://www.linkedin.com/oauth/v2/authorization', params = params)
webbrowser.open('https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=81u411hl9z91tg&redirect_uri=http://localhost:4200/profile/&state=DCEeFWf45A53sdfKef424s&scope=r_fullprofile%20r_emailaddress%20w_member_social')
# print(res)