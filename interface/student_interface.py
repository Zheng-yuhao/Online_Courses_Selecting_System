from db import models
from interface import common_interface


# 学生注册interface
def student_register_interface(user, pwd):
    # 1. 先确认学生是否存在
    stu_obj = models.Student(user, pwd)
    re = stu_obj.select(user)

    # 2. 若存在,返回None提示用户已存在请重新输入id
    if re:
        return False, f'用户名{user}已存在,无法再次注册'

    # 3. 若不存在,学生obj调用save,并且save
    stu_obj.save()
    return True, f'用户名{user}注册成功!'


# 学生登录interface
def student_login_interface(user, pwd):
    # 1. 先查看用户是否存在
    stu_obj = models.Student(user, pwd)
    re = stu_obj.select(user)

    # 2. 存在的话返回True
    if re:
        return True, f'用户{user}登录成功'
    # 3. 不存在的话返回False调用register函数
    return False, f'无{user}用户,请先注册'


# 学生选择学校interface
def student_school_chosen_interface(school_name, user_name):
    # 先取出学生obj
    stu_obj = models.Student.select(user_name)

    # 再用学生obj调用课程的列表
    course_list = stu_obj.course_chosen_list
    course_list.append(school_name)
    # 再保存
    stu_obj.save()
    return True, f'校区名{school_name}选择成功'


# 学生选择课程(先选择校区再选择校区中的某一门课)
def student_course_choice_interface(school_name, user_name):
    while True:
        school_obj = models.School.select(school_name)
        course_list = school_obj.course_list
        for index, course_name in enumerate(course_list):
            print(f'编号:{index}, 课程名:{course_name}')

        course_choice = input(f'请选择当前校区名为{school_name}下的课程 >>> : ').strip()
        if not course_choice.isdigit():
            print('请输入数字形式')
            continue

        course_choice = int(course_choice)
        course_name = course_list[course_choice]

        stu_obj = models.Student.select(user_name)
        stu_obj.course_chosen_list.append(course_name)
        stu_obj.save()

        cour_obj = models.Course.select(course_name)
        cour_obj.student_list.append(user_name)
        cour_obj.save()

        return True, f'学生{user_name}选择了校区为{school_name}中的课程名称为{course_name}, 成功'


# 学生查看成绩interface
def student_check_interface(user_id):
    stu_obj = models.Student.select(user_id)
    if stu_obj:
        return True, stu_obj.score
    return False, f'你还没有参加考试呢' # 这里以后考虑一下如何通过课程和学习关联成绩




