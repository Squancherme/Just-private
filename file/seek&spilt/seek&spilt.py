import pickle
def save_file(boy, girl, count):
    boy_file = 'boy_' + str(count) + '.txt'
    girl_file = 'girl_' + str(count) + '.txt'

    f = open(boy_file, 'wb')
    f2 = open(girl_file, 'wb')

    pickle.dump(boy, f)
    pickle.dump(girl, f2)
    #f.writelines(boy)
    #f2.writelines(girl)

    f.close()
    f2.close()

def spilt_file(main_file):
    f3 = open(main_file)
    boy = []
    girl = []
    count = 0
    for each_line in f3:
        if each_line[:6] == '======':
            count += 1
            save_file(boy, girl, count)
            boy = []
            girl = []
        else:
            speaker, words = each_line.split(':', 1)
            if speaker == '小甲鱼':
                boy.append(words)
            if speaker == '小客服':
                girl.append(words)
    count += 1
    save_file(boy, girl, count)
spilt_file(r'.\record.txt')
    
