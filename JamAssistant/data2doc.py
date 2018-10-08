import json
import shutil

from JamAssistant.Jamconfig import *

testdata_dic = {'编号': '001', '院系': '机电与信息工程', '学号': '201600800481',
                '姓名': '李威宇', '性别': '男', '出生年月': '1998.10.31',
                '政治面貌': '中共预备党员', '民族': '汉族', '入学时间': '2019.9',
                '专业': '计算机科学与技术（中澳合作）', '学制': '四年制', '联系电话': '15608291615',
                '身份证号': '513701199810311715',
                '名次': '10', '总人数': '110', '必修课': '10', '及格': '10', '综合排名': '2', '综合总人数': '110',
                '获奖时间一': '2017', '奖项名称一': '山东大学（威海）优秀学生一等奖学金', '颁奖单位一': '蓝桥杯组委会',
                '获奖时间二': '2018', '奖项名称二': '蓝桥杯1', '颁奖单位二': '高等学校大学外语教学指导委员会',
                '获奖时间三': '2019', '奖项名称三': '蓝桥杯2', '颁奖单位三': '蓝桥杯组委会2',
                '获奖时间四': '2020', '奖项名称四': '蓝桥杯3', '颁奖单位四': '蓝桥杯组委会3',
                '申请理由': '测试申请理由', '推荐理由': '测试推荐理由', '院系意见': '测试院系意见'
                }
template_dic = {'编号': '@No', '院系': '所在院系模板', '学号': '学号模板',
                '姓名': '姓名模板', '性别': '性别模板', '出生年月': '生日模板',
                '政治面貌': '政治面貌模板', '民族': '民族模板', '入学时间': '入学时间模板',
                '专业': '专业模板', '学制': '学制模板', '联系电话': '联系电话模板',
                '身份证号': 'xxxxxxxxxxxxxxxxxx',
                '名次': '#1', '总人数': '#2', '必修课': '#3', '及格': '#4', '综合排名': '#5', '综合总人数': '#6',
                '获奖时间一': '获奖一', '奖项名称一': '奖项名称一', '颁奖单位一': '颁奖单位一',
                '获奖时间二': '获奖二', '奖项名称二': '奖项名称二', '颁奖单位二': '颁奖单位二',
                '获奖时间三': '获奖三', '奖项名称三': '奖项名称三', '颁奖单位三': '颁奖单位三',
                '获奖时间四': '获奖四', '奖项名称四': '奖项名称四', '颁奖单位四': '颁奖单位四',
                '申请理由': '申请理由模板', '推荐理由': '推荐理由模板', '院系意见': '院系意见模板'
                }
font_dic = {'机械设计制造及其自动化': '22',
            '机械设计制造及其自动化（中澳合作）': '16',
            '计算机科学与技术（中澳合作）': '20',
            '山东大学（威海）优秀学生一等奖学金': '22',
            '山东大学（威海）优秀学生二等奖学金': '22',
            '山东大学（威海）优秀学生三等奖学金': '22',
            '高等学校大学外语教学指导委员会': '22'
            }


def super_replace(doc, item, key_word, font_size):
    # super_temp = '<w:r><w:rPr><w:rFonts w:hint="eastAsia"/><w:sz w:val="24"/></w:rPr><w:t>' + item + '</w:t></w:r>'
    super_temp = '<w:sz w:val="24"/></w:rPr><w:t>' + item + '</w:t></w:r>'
    super_str = super_temp.replace('24', font_size)
    super_str = super_str.replace(item, key_word)

    doc = doc.replace(super_temp, super_str)
    return doc


def data2json(data_dic):
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as json_reader:
            isExist = False
            json_data = json_reader.readlines()
            for i in range(len(json_data)):
                stu_data = json.loads(json_data[i])
                if stu_data['编号'] == data_dic['编号']:
                    json_data[i] = json.dumps(data_dic, ensure_ascii=False) + '\n'
                    isExist = True
            json_reader.close()

            if not isExist:
                json_data.append(json.dumps(data_dic, ensure_ascii=False) + '\n')
            json_data = "".join(json_data)
            with open(json_file, 'w', encoding='utf-8') as json_writer:
                json_writer.write(json_data)
                json_writer.close()
    else:
        with open(json_file, 'w', encoding='utf-8') as json_writer:
            json_data = json.dumps(data_dic, ensure_ascii=False)
            json_writer.write(json_data + '\n')
            json_writer.close()


def data2xml(data_dic, filename):
    data2json(data_dic)
    stu_dept = data_dic['院系']
    dept_dir = os.path.join(BASE_DIR, 'JamAssistant', 'students', stu_dept)
    file_path = os.path.join(file_dir, filename)
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)

    if data_dic['政治面貌'] == '中共预备党员':
        if data_dic['学号'].startswith('2017'):
            template_path = template2017yubei_path
        else:
            template_path = template2016yubei_path
    else:
        if data_dic['学号'].startswith('2017'):
            template_path = template2017_path
        else:
            template_path = template2016_path

    with open(template_path, 'r', encoding='utf-8') as template:
        doc = template.read()
        for item in data_dic:
            if data_dic[item].endswith("2016") or \
                    data_dic[item].endswith("2017") or \
                    data_dic[item].endswith("2018"):
                data_dic[item] = data_dic[item][:-4]

            if data_dic[item] is None:
                data_dic[item] = ''
            elif item == '身份证号':
                for i in range(len(data_dic[item]) - 1, -1, -1):
                    doc = doc.replace('I' + str(i + 1), data_dic[item][i])
            elif item == '专业' and (data_dic[item] == '机械设计制造及其自动化' or
                                   data_dic[item] == '机械设计制造及其自动化（中澳合作）' or
                                   data_dic[item] == '计算机科学与技术（中澳合作）'):
                doc = super_replace(doc, template_dic[item], data_dic[item], font_dic[data_dic[item]])
            elif (data_dic[item] == '山东大学（威海）优秀学生一等奖学金' or
                  data_dic[item] == '山东大学（威海）优秀学生二等奖学金' or
                  data_dic[item] == '山东大学（威海）优秀学生三等奖学金'):
                doc = super_replace(doc, template_dic[item], data_dic[item], font_dic[data_dic[item]])
            elif (data_dic[item] == '高等学校大学外语教学指导委员会'):
                doc = super_replace(doc, template_dic[item], data_dic[item], font_dic[data_dic[item]])
            else:
                doc = doc.replace(template_dic[item], data_dic[item])

        template.seek(0, 0)
        with open(file_path, 'w', encoding='utf-8') as out:
            out.write(doc)
            out.close()
    template.close()
    if not os.path.exists(dept_dir):
        os.mkdir(dept_dir)
    shutil.copy(file_path, dept_dir)


if __name__ == '__main__':
    data2xml(testdata_dic, '1.doc')
