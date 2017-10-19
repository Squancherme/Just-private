#遍历删除
#未指定文件夹（当前目录操作）

import os.path
import os

file_name = []
while True:
    name = input('输入文件名（包括后缀，‘：wq退出’）：')
    if name != ':wq':
        file_name.append(name)
    else:
        break
    
for i,d,e in os.walk(os.curdir):
    for g in e:
        g = str(g)

        if g in file_name:
            os.remove(os.path.join(i,g))
            print('已移除：',g)
            
