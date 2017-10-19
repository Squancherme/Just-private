#打开文件

import os
os.chdir(os.curdir)
file = os.listdir(os.curdir)
count_py = 0
count_txt = 0

for each_file in file:
    if os.path.splitext(each_file)[1] == '.py':
        #print(each_file)
        
        with open(each_file, encoding='utf-8') as file:
            for each_line in file:
                count_py += 1
        
    if os.path.splitext(each_file)[1] == '.txt':
        f = open(each_file, encoding = 'utf-8')
        for each_line in f:
            count_txt += 1
        f.close()
        
print('.txt:',count_txt)
print('.py',count_py)
