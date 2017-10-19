#需要安装request库

import requests  
import re  
  
login_url  = 'https://github.com/login'  
user = 'yx.fidei@outlook.com' # // 具体账号  
password  = '91506991x.'  # // 具体密码  
user_headers = {  
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
#'Cookie':r,
'Host':'github.com',
'Referer':'https://github.com/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' 
}  
  
session  = requests.Session()  
response = session.get(login_url, headers = user_headers)  
 
html = response.content.decode('utf8')
a = html.find('authenticity_token" type="hidden" value="')

  
login_data = {      
    'commit' : 'Sign in',      
    'utf8' : '✓',      
    'login' : user,      
    'password' : password  
}  
login_data['authenticity_token'] = html[a+41:a+129] 
session_url  = 'https://github.com/session'  
response = session.post(session_url, headers = user_headers, data = login_data) 
  
#indexhtml = session .get('https://github.com/HanlaoTwo/StacknotOverFlow',headers=header)#可以继续用这个会话对象去访问需要登录的页面  
#print(indexhtml.text)  
l = response.content.decode('utf8')
print(l)
response2 = session.get('https://github.com/')
l2 = response2.content.decode('utf8')
response3 = session.get('https://github.com/marketplace')
l3 = response3.content.decode('utf8')
print(l3)
