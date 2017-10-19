import urllib.request
import http.cookiejar as cook

url = 'https://github.com/login'
url2 = 'https://github.com/session'

cookie = cook.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
openner = urllib.request.build_opener(handler)
openner.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]

q = openner.open(url)
html = q.read().decode('utf8')
a = html.find('authenticity_token" type="hidden" value="')

data ={
    'commit':'Sign in',
    'utf8':'✓',
    'login':'yx.fidei@outlook.com',
    'password':'91506991x.'
    }
data['authenticity_token'] = html[a+41:a+129]
data = urllib.parse.urlencode(data).encode('utf-8')


w = openner.open(url2,data)
t = w.read().decode('utf8')
print(t)



'''url = 'https://github.com/login'
req1 = urllib.request.Request(url)
req1.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
response = urllib.request.urlopen(req1)
html = response.read().decode('utf-8')
a = html.find('authenticity_token" type="hidden" value="')

data ={
    'commit':'Sign in',
    'utf8':'✓',
    'login':'yx.fidei@outlook.com',
    'password':'91506991x.'
    }
data['authenticity_token'] = html[a+41:a+129]
data = urllib.parse.urlencode(data).encode('utf-8')

url2 = 'https://github.com/session'
req2 = urllib.request.Request(url2, data)
req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

response1 = opener.open(req2)'''
