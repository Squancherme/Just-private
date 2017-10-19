#当前目录递归查找.txt关键字

import os
def is_txt(file, key):
    f = open(file)
    count = 0
    s = []
    tem = 0
    dictionary = {}
    
    for each_line in f:
        count += 1
        if key in each_line:
            tem = each_line.find(key, tem)
            s.append(tem+1)
            while tem != -1:
                tem = each_line.find(key, tem+1)
                if tem != -1:
                    s.append(tem+1)
            dictionary[count] = s
        s = []  
        tem = 0    
    f.close()
    #print(s)
    return dictionary
    

def find_file(key):
    all_file = os.walk(os.getcwd())
    for i in all_file:
        for file_ in i[2]:
            if os.path.splitext(file_)[1] == '.txt':
                file = os.path.join(i[0],file_)
                dictionary = is_txt(file, key)
                
                print('=============================================')
                print(file)
                go(dictionary)
          
def go(dictionary):
    keys = dictionary.keys()
    keys = sorted(keys)
    for i in keys:
        print('在第',i,'行'    '第',str(dictionary[i]),'个')

        
key = input('关键字是：')
find_file('x')
input()
