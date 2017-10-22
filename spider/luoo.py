import os
import urllib.request
import re
import tkinter
import PIL.ImageTk
import PIL.Image
    
#查询最新期刊
def search_():
    req = urllib.request.Request('http://www.luoo.net/')
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode()

    num = re.search('title">(vol\.(\d{3,4}) \w+?)<', html)
    index = re.search('http://www.luoo.net/vol/index/(\d{4})',html)

    return num.group(1), num.group(2), index.group(), index.group(1)

#对比是否最新期刊
def compare():
        
    with open(r'luoo/compare.txt', 'a+') as f1:
        f1.seek(0)
        file = f1.read()
        name  = tem2[0]
        music = tem[1]
        a = ''
        for i in music:
            a = a + i + '\n'

        if name in file:
            print('还没更新,还是',name)
            root = tkinter.Tk()
            root.title(name)
            textLabel1 = tkinter.Label(root,
                                text = a,
                                justify=tkinter.LEFT,
                                padx=10)
            textLabel1.pack()
            im = PIL.Image.open('luoo/'+name+'.jpg')
            tkimg=PIL.ImageTk.PhotoImage(im)
            imgLabel = tkinter.Label(root, image=tkimg)
            imgLabel.pack()
            root.mainloop()
            download_ = False

        else:
            while True:
                print('更新了:',name)
                root = tkinter.Tk()
                root.title(name)
                textLabel1 = tkinter.Label(root,
                                    text = a,
                                    justify=tkinter.LEFT,
                                    padx=10)
                textLabel1.pack()
                im = PIL.Image.open('luoo/'+name+'.jpg')
                tkimg=PIL.ImageTk.PhotoImage(im)
                imgLabel = tkinter.Label(root, image=tkimg)
                imgLabel.pack()
                root.mainloop()
                key =input('下不下？(y/n)')
                
                if key == 'y':
                    download_ = True
                    break

                if key == 'n':
                    download == False
                    break

                if key!='y' or key!='n':
                    print('输错了')
            
            f1.seek(0, 2)
            f1.write(name)

        return download_

#下载
def download():
      if compare():
            count = -1
            tem = tem[1]
            pic = tem2[0]
            
            for url in tem[0]:
                  count +=1
                  name = tem[count]
                  print('正在下:',name,'...')
                  local_path = 'luoo/' +name + '.mp3'
                  #req = urllib.request.Request(url)
                  #req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
                  urllib.request.urlretrieve(url,local_path)
                  print('完成')
                  
            picture = 'luoo/' + pic + '.jpg'
            print('正在下:', pic + '.jpg')
            urllib.request.urlretrieve(tem[2],picture)
            print('都下完了')
            
#获取表单
def get_list():
    url_list = []
    req = urllib.request.Request(tem2[2])
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode()

    picture = re.search('http://img-cdn2.luoo.net/.+?.jpg', html)
    music_list = re.findall('trackname btn-play">(\d{1,2}\. .+?)<', html)
    music_num = re.findall('\d{1,2}', str(music_list))

    for num in music_num:
        url = 'http://mp3-cdn2.luoo.net/low/luoo/radio' + tem2[1] + '/' + str(num) + '.mp3'
        url_list.append(url)
    return url_list, music_list, picture.group()

tem2 = search_()
tem = get_list()


if __name__ == "__main__":
    download()

input('输入任何')
