import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.twitch.tv/')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('ok')
    print(site.read())
