#查找target中格式的文件(当前目录递归查找)
import os
def search_file(start_dir,target):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            video_list.append(os.getcwd() + os.sep + each_file + os.linesep)

        if os.path.isdir(each_file):
            search_file(each_file, target)
            os.chdir(os.pardir)

start_dir = input()
program_dir = os.getcwd()

target = ['.mp4', '.avi', '.rmvb']
video_list = []
search_file(start_dir, target)
