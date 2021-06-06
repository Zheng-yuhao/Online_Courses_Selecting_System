import os
from conf import settings



def get_all_school_interface():
    school_dir = os.path.join(settings.DB_PATH,'School')

    if not os.path.exists(school_dir):
        return False, f'没有相关学校文件,请联系管理员'

    school_list = os.listdir(school_dir)
    return True, school_list


def get_all_course_interface():
    course_dir = os.path.join(settings.DB_PATH,'Course')

    if not os.path.exists(course_dir):
        return False, f'没有相关学校文件,请联系管理员'

    school_list = os.listdir(course_dir)
    return True, course_list