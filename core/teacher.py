from interface import teacher_interface
from interface import common_interface


teacher_info = {
    'user':None
}


# Teacher's login function
def login():
    print('login function is working >>> ')
    while True:
        user = input('Please enter your user_id').strip()
        pwd = input('Please enter your password').strip()
        re_pwd = input('Please enter your password again').strip()

        if pwd == re_pwd:
            flag, msg = teacher_interface.teacher_login_interface(user,pwd)
            if flag:
                print(msg)
                teacher_info['user'] = user
                break
            else:
                print(msg)


# Check teacher's course_list function
def check_course_list():
    while True:
        print('Checking the course list >>> ')
        flag, msg = teacher_interface.teacher_check_list_interface(teacher_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)



# Select course teacher wants to take in
def select_course():
    while True:
        print('Preparing the course list >>> ')
        flag, msg= common_interface.get_all_course_interface()
        if flag:
            for index, course_name in enumerate(msg):
                print(f'{index} > Course_name : {course_name}')

            choice = input('Enter your choice (You must enter the numerical type!)').strip()
            if not choice.isdigit():
                print('Please enter the numerical type!')
                continue
            choice = int(choice)
            course_name = msg[choice]
            flag, msg = teacher_interface.teacher_select_course_interface(course_name, teacher_info.get('user'))
            if flag:
                print(msg)
                break


# Check the student in selected course
def check_student():
    while True:
        print('Checking the student list >>> ')
        flag, msg = common_interface.get_all_course_interface()
        if flag:
            for index, course_name in enumerate(msg):
                print(f'{index} > Course_name : {course_name}')

            choice = input('Choosing the course number . ')
            choice = int(choice)
            course_name = msg[choice]
            flag, msg = teacher_interface.teacher_check_student_interface(course_name)
            if flag:
                print(msg)
                break

# Modify student's grades
# def modify_grades():
#     while True:
#         print('Preparing the students list >>> ')
#


func_dict = {
    '1':login,
    '2':check_course_list,
    '3':select_course,
    '4':check_student,
    '5':None
}

def teacher_view():
    while True:
        print(
            '''
            === 欢迎来到老师系统 ===
                - 1.登录
                - 2.查看课程
                - 3.选择课程
                - 4.查看课程下学生
                - 5.修改分数
            ===      end      ===
            '''
        )
        choice = input('请选择管理员系统的选项进行操作 >>> : ')
        if choice not in func_dict:
            print('没有此选项请重新输入')
            continue

        func_dict[choice]()