#保存一个网站源代码到当前目录(html.txt)

import os
import urllib.request
a = input('输入网址')
url = a

req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')



with open('html.txt','w') as f:
        f.write(html)
