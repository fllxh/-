import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_dir = os.path.join(BASE_DIR, 'JamAssistant', 'students', '全校学生')

template2016_path = os.path.join(BASE_DIR, 'JamAssistant', 'template2016.xml')
template2017_path = os.path.join(BASE_DIR, 'JamAssistant', 'template2017.xml')
template2016yubei_path = os.path.join(BASE_DIR, 'JamAssistant', 'template2016_yubei.xml')
template2017yubei_path = os.path.join(BASE_DIR, 'JamAssistant', 'template2017_yubei.xml')

award_file = os.path.join(BASE_DIR, 'JamAssistant', 'JamList.csv')
json_file = os.path.join(BASE_DIR, 'JamAssistant', 'students.json')
