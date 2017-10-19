import urllib.request
import urllib.parse
def log_in():
    url = 'http://221.10.255.233:8088/showlogin.do?ssid=pppoe&url=http://www.baidu.com/'
    data ={
    'ssid':'pppoe',
    'url':'http://www.msftconnecttest.com/redirect'
        }
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url, data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    print(html)
    a = html.find('''CSRFToken_HW' value=''')
    CSRFToken_HW = html[a+21:a+53]
    b = html.find('''20171016''')
    loggerId = html[b:b+17]


    data2 = {
    'username':'02803095689',
    'password':'000000',
    'wlanuserip':'101.204.89.67',
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
    print(type(req2))
    req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

    response2 = urllib.request.urlopen(req2)

    html2 = response2.read().decode('utf-8')
    
    
    a = html2.find('CSRFToken_HW')
    b = html2.find('loggerId')
    c = html2.find('ATTRIBUTE_UUID')
    d = html2.find('<title>')
    print(html2[d:d+20])
    
    data3 ={
    'ATTRIBUTE_UUID' : 'html[c+15:c+47]',
    'loggerId' : 'html[b+9:b+26]',
    'CSRFToken_HW' : 'html[a+13:a+45]',
    'username':'02803095689',
    'wlanacname':'longquanhx',
    'wlanuserip':'101.204.90.142'
    }
    data3 = urllib.parse.urlencode(data3)
    print(data3)
    return data3
tem = log_in()

def log_out(tem):
    url = 'http://221.10.255.233:8088//LogoutServlet'
    response = urllib.request.urlopen(url + '?' + tem)
