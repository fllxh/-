import csv
import os

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.utils.http import urlquote

from JamAssistant import data2doc
from JamAssistant.Jamconfig import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.

def index(request):
    csvFile = open(award_file, 'r', encoding='utf-8')
    reader = csv.reader(csvFile)
    jam_list = []
    for item in reader:
        jam_list.append(item)
    csvFile.close()

    if request.method == "POST":
        student_no = request.POST.get("stu_no")
        student_sno = request.POST.get("stu_sno")
        student_dept = request.POST.get("stu_dept")
        student_name = request.POST.get("stu_name")
        student_sex = request.POST.get("stu_sex")

        student_birthday = request.POST.get("stu_bir")
        student_bir = student_birthday.split('-')
        student_birthday = student_bir[0] + '年' + str(int(student_bir[1])) + '月'

        student_poli = request.POST.get("stu_poli")
        student_nation = request.POST.get("stu_nation")
        student_month = request.POST.get("stu_month")
        student_majority = request.POST.get("stu_major")
        student_length = request.POST.get("stu_len")
        student_telphone = request.POST.get("stu_tel")
        student_id = request.POST.get("stu_id")
        student_p1 = request.POST.get("stu_p1")
        student_p2 = request.POST.get("stu_p2")
        student_p3 = request.POST.get("stu_p3")
        student_p4 = request.POST.get("stu_p4")
        student_p5 = request.POST.get("stu_p5")
        student_p6 = request.POST.get("stu_p6")

        student_awardname1 = request.POST.get("stu_awardname1")
        student_awardname2 = request.POST.get("stu_awardname2")
        student_awardname3 = request.POST.get("stu_awardname3")
        student_awardname4 = request.POST.get("stu_awardname4")

        student_awarddate1 = ''
        student_awarddate2 = ''
        student_awarddate3 = ''
        student_awarddate4 = ''
        student_awardunit1 = ''
        student_awardunit2 = ''
        student_awardunit3 = ''
        student_awardunit4 = ''
        for award in jam_list:
            if student_awardname1 in award:
                student_awarddate1 = award[2]
                student_awardunit1 = award[1]
            elif student_awardname2 in award:
                student_awarddate2 = award[2]
                student_awardunit2 = award[1]
            elif student_awardname3 in award:
                student_awarddate3 = award[2]
                student_awardunit3 = award[1]
            elif student_awardname4 in award:
                student_awarddate4 = award[2]
                student_awardunit4 = award[1]

        student_reason1 = request.POST.get("stu_reason1")
        student_reason2 = request.POST.get("stu_reason2")
        student_reason3 = request.POST.get("stu_reason3")

        data_dic = {'编号': student_no, '院系': student_dept, '学号': student_sno,
                    '姓名': student_name, '性别': student_sex, '出生年月': student_birthday,
                    '政治面貌': student_poli, '民族': student_nation, '入学时间': student_month,
                    '专业': student_majority, '学制': student_length, '联系电话': student_telphone,
                    '身份证号': student_id,
                    '名次': student_p1, '总人数': student_p2, '必修课': student_p5, '及格': student_p6, '综合排名': student_p3,
                    '综合总人数': student_p4,
                    '获奖时间一': student_awarddate1, '奖项名称一': student_awardname1,
                    '颁奖单位一': student_awardunit1,
                    '获奖时间二': student_awarddate2, '奖项名称二': student_awardname2,
                    '颁奖单位二': student_awardunit2,
                    '获奖时间三': student_awarddate3, '奖项名称三': student_awardname3,
                    '颁奖单位三': student_awardunit3,
                    '获奖时间四': student_awarddate4, '奖项名称四': student_awardname4,
                    '颁奖单位四': student_awardunit4,
                    '申请理由': student_reason1, '推荐理由': student_reason2, '院系意见': student_reason3
                    }
        if student_name is None or student_name is '':
            student_name = 'lackOfname'

        # 判断是否第一次填写
        if not os.path.exists(
                os.path.join(file_dir, student_no + student_name + '.doc')):
            filename = student_no + student_name + '.doc'
        else:
            cnt = 0
            for item in os.listdir(file_dir):
                if item.startswith(student_no + student_name):
                    cnt += 1
            filename = student_no + student_name + r'版本' + str(cnt) + '.doc'

        data2doc.data2xml(data_dic, filename)

        def file_iterator(file_name, chunk_size=512):
            with open(file_name, encoding='utf-8') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break

        the_file_path = os.path.join(file_dir, filename)
        response = HttpResponse(file_iterator(the_file_path),
                                content_type='APPLICATION/OCTET-STREAM')
        response['Content-Disposition'] = 'attachment;filename="%s"' % (urlquote(filename))
        response['Content-Length'] = os.path.getsize(the_file_path)
        return response
    else:
        return render(request, 'JamAssistantIndex.html', )
