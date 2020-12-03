import json
from JamAssistant.data2doc import data2doc
from JamAssistant.Jamconfig import *


def checkFile(file_path, start, end):
    for id in range(start, end):
        for root, dirs, files in os.walk(file_path):
            isExist = 0
            for file in files:
                if file.startswith(str(id)):
                    isExist += 1
            if not isExist:
                print('未填编号' + str(id))
            if isExist >= 2:
                print('重复编号' + str(id))


def formatFile(file_path):
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith('版本1.doc') or \
                    file.endswith('版本2.doc') or \
                    file.endswith('版本3.doc'):
                os.rename(file_path + '\\' + file, file_path + '\\' + file[:-7] + '.doc')


def json2doc(json_file):
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as json_reader:
            json_data = json_reader.readlines()
            for i in range(len(json_data)):

                stu_data = json.loads(json_data[i])
                student_no = stu_data['编号']
                student_name = stu_data['姓名']
                if not os.path.exists(
                        os.path.join(file_dir, student_no + student_name + '.doc')):
                    filename = student_no + student_name + '.doc'
                else:
                    cnt = 0
                    for item in os.listdir(file_dir):
                        if item.startswith(student_no + student_name):
                            cnt += 1
                    filename = student_no + student_name + r'版本' + str(cnt) + '.doc'

                data2doc(stu_data, filename)

            json_reader.close()


if __name__ == '__main__':
    file_path = '全校学生'
    json_file = '..\\students.json'
    start = 358
    end = 535
    # checkFile(file_path, start, end)
    # formatFile(file_path)
    json2doc(json_file)
