import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_dir = os.path.join(BASE_DIR, 'JamAssistant', 'students', '全校学生')

template2018_path = os.path.join(BASE_DIR, 'JamAssistant', 'template2018.xml')
template2017_path = os.path.join(BASE_DIR, 'JamAssistant', 'template2017.xml')
template2018yubei_path = os.path.join(BASE_DIR, 'JamAssistant', 'template2018_yubei.xml')
template2017yubei_path = os.path.join(BASE_DIR, 'JamAssistant', 'template2017_yubei.xml')
template_zishiying = os.path.join(BASE_DIR, 'JamAssistant', 'template_zishiying.xml')


award_file = os.path.join(BASE_DIR, 'JamAssistant', 'JamList.csv')
json_file = os.path.join(BASE_DIR, 'JamAssistant', 'students.json')
