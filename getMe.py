import requests
import webbrowser

# params = dict(Connection='Keep-Alive', oauth2_access_token='AQR6o7JcTgFN-U_Nx1I3oxluLTit8XL44ZsO3_BOkKqh-m9pI0N5W8OplwXWid-HU-Rz9s6RI-ufOuIxAtFEzKYBROuEA_5xPrj4C6_ECqjW9lK3sXPi2E4zhqsftM5wtnthJJ89m6LfhQc6aUh9dekpx6NTKFg2tprN6Rsv81kcE31vPUXxoe6F6tJUKg')

res = requests.get('https://api.linkedin.com/v2/me',
                    headers={"Authorization":"Bearer AQUzUMWlqKXW3XE1-9u-bfe6kG6JzqT1jh_VGuIoxxa_5lfpU-LXJbYMeL0d1bKEWJ1mL-XDRVw1ZnZP3EGWw7pK6-fKhedLIT_OuZGzJBNJMBDvraoWZ_QVC0jt_NBWnyNSQeHj9CHqjkBqgAA1ZX0T_XfHp8OksUmYClBILS-MG8iEFjyLMTKP2rz7hlngDDV2qAVmQTqARU9nYM7DVc-pQ_K9lCDFpEMo9OPeVUpq3uTztD6Vfo4W1el7fpGrB_7_648WVjEEL0bUKQdZCumcerpZV5lsi7GoO5Yej54BMD4tuwnEF7nI-8ileHjMZhYhEr1aC54DGZgjIpw1QYkS06ryUg",
                             "Connection": "'Keep-Alive'"}).json()
# webbrowser.open('https://www.linkedin.com//v2/me?Connection=Keep-Alive&Authorization=AQSVx7cxjiZFsH-rBmIWzXBkTDJTOmVU7RY6hTDb2pachGhX4ChJpy1tfmAH4X072QzvUzv7xK5RqaxUgQ4QhloxJcG-9Qa9bNHG1qm1zDOJTDm3I9bn0VKgmmX1yeiuWK-0WCkHIlV-4EXbOmNHwANoVyg9Xl4A6GDG7ZAQohG6EVozKJ8peHoNEffE-g')
print(res)