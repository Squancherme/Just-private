import urllib.request
import urllib.parse
url = 'http://221.10.255.233:8088/showlogin.do?ssid=pppoe&url=http://www.msftconnecttest.com/redirect'
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

a = html.find('''CSRFToken_HW' value=''')
CSRFToken_HW = html[a+21:a+53]
b = html.find('''20171018''')
loggerId = html[b:b+17]


data2 = {
'username':'02803095689',
'password':'000000',
'wlanuserip':'101.204.90.142',
'wlanacname':'',
'wlanmac':'',
'firsturl':'http://www.baidu.com',
'ssid':'pppoe',
'userAgent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
'usertype':'pc',
'gotopage':'/GWlanRes/pppoe/LoginURL/pc/index.jsp',
'successpage':'/GWlanRes/pppoe/OnlineURL/pc/index.jsp'
}
url2 = 'http://221.10.255.233:8088//LoginServlet'
data2['CSRFToken_HW'] = CSRFToken_HW
data2['loggerId'] = loggerId
data2 = urllib.parse.urlencode(data2).encode('utf-8')

req2 = urllib.request.Request(url2, data2)
#print(type(req2))
req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

response2 = urllib.request.urlopen(req2)
html2 = response2.read().decode('utf-8')
print(html2)
