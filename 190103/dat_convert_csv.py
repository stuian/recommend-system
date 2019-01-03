# _*_ coding:utf-8 _*_
import os

path_0 = r"E:\github\recommend-system\190103\data"

path_1 = r"E:\github\recommend-system\190103"

filelist = os.listdir(path_0)

for files in filelist:

    dir_path = os.path.join(path_0, files)
    # 分离文件名和文件类型
    file_name = os.path.splitext(files)[0]  # 文件名
    file_type = os.path.splitext(files)[1]  # 文件类型

    print(dir_path)
    file_test = open(dir_path, 'r')
    # 将.dat文件转为.csv文件
    new_dir = os.path.join(path_1, str(file_name) + '.csv')

    print(new_dir)

    file_test2 = open(new_dir, 'w')

    for lines in file_test.readlines():
        str_data = ",".join(lines.split('::'))
        file_test2.write(str_data)
    file_test.close()
    file_test2.close()