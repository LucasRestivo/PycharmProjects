import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.9gag.com/')
except urllib.error.URLError:
    print('Site indisponível')
else:
    print('Tudo Ok')
    print(site.read())
