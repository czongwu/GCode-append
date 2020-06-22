# -*- coding: utf-8 -*-
import os

# f_name = 'D:/模型/木模/2020/6-8/过渡法兰.NC'
# f_new_name = "%s.new" % f_name
# old_str = 'N0010 G40 G17 G90 G71'
#
# f_new = open(f_new_name, 'w', encoding='utf-8')
# with open(f_name, 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         if old_str in line:
#             line = line.replace(' ', ' G55 ', 1)
#         f_new.write(line)
# f_new.close()
path_1 = 'E:\Develop\python\GCode-append\\test\凯达G30XH_1.NC'
# path_2 = 'E:\Develop\python\GCode-append\\test\凯达G30XH_2.NC'
path_3 = 'E:\Develop\python\GCode-append\\test\凯达G30XH_3.NC'
# path_4 = 'E:\Develop\python\GCode-append\\test\凯达G30XH_4.NC'
path_5 = 'E:\Develop\python\GCode-append\\test\凯达G30XH_5.NC'
k = [path_1, '', path_3, '', path_5]


def write_file(path, GCode):
    f_name = path
    f_new_name = "%s.new" % f_name
    old_str = 'N0010 G40 G17 G90 G71'
    f_new = open(f_new_name, 'w', encoding='utf-8')
    with open(f_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if old_str in line:
                line = line.replace(' ', GCode, 1)
            f_new.write(line)
        f_new.close()
        f.close()
        os.remove(f_name)
        os.rename(f_new_name, f_name)


for index, p in enumerate(k):
    if index == 0:
        if p != '':
            write_file(p, GCode=' G55 ')
        else:
            print('G55 路径为空')
    elif index == 1:
        if p != '':
            write_file(p, GCode=' G56 ')
        else:
            print('G56 路径为空')
    elif index == 2:
        if p != '':
            write_file(p, GCode=' G57 ')
        else:
            print('G57 路径为空')
    elif index == 3:
        if p != '':
            write_file(p, GCode=' G58 ')
        else:
            print('G58 路径为空')
    elif index == 4:
        if p != '':
            write_file(p, GCode=' G59 ')
        else:
            print('G59 路径为空')
