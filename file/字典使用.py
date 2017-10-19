#使用字典

def begin():
    print('-----1.查看通讯录-----')
    print('-----2.增添通讯录-----')
    print('-----3.删除通讯录-----')
    print('-----4.退出通讯录-----')
    #print('-----5.查看所有-----')
    print('输入指令')
    tem = int(input())
    if tem == 1:
        check()
    if tem == 2:
        add()
    if tem == 3:
        del_()
    if tem == 4:
        print('再见')
    
dictionary = {}

def check():
    global dictionary
    name = input('输入名字：')
    if name in dictionary:
        print('姓名：',name)
        print(dictionary[name])
        begin()
        
    else:
        print('用户不存在')
        begin()
        
def add():
    global dictionary
    tem =  input('输入要添加的名字：')
    tem2 = int(input('输入要添加的号码：'))
    if tem in dictionary:
        while True:
            tem3 = input('已存在，修改吗？ yes/no')
            if tem3 == 'yes':
                dictionary[tem] = tem2
                print(dictionary[tem])
                break
            
            else:
                print('输入yes/no')
        begin()
    else:
        dictionary[tem] = tem2
        print(tem + ':'+ str(tem2))
        begin()
def del_():
    global dictionary
    tem4 = input('输入要删的名字：')
    if tem4 in dictionary:
        dictionary.pop(tem4)
        begin()
begin()
