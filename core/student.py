from interface import student_interface
from interface import common_interface
from lib import common

student_info = {
    'user' : None
}


# 学生注册功能
def register():
    while True:
        print('学生注册功能正在运行 >>> : ')

        user = input('请输入用户名 ： ')
        pwd = input('请输入密码 ： ')
        re_pwd = input('请再次输入密码 ： ')

        if not pwd == re_pwd:
            print('请重新输入,两次密码不一致')
            continue

        flag, msg = student_interface.student_register_interface(user, pwd)

        if flag:
            print(msg)
            break
        else:
            print(msg)


# 学生登录功能
def login():
    while True:
        print('学生登录功能正在运行 >>> : ')

        user = input('请输入用户名 ： ')
        pwd = input('请输入密码 ： ')
        re_pwd = input('请再次输入密码 ： ')

        if not pwd == re_pwd:
            print('请重新输入,两次密码不一致')
            continue

        flag,msg = student_interface.student_login_interface(user,pwd)
        if flag:
            print(msg)

            student_info['user'] = user
            break

        else:
            print(msg)
            register()



# 学生选择校区功能
@common.auth('student')
def select_school():
    while True:
        print('学生选择校区功能启动 >>>')
        msg, re = common_interface.get_all_school_interface()

        for index, school_name in enumerate(re):
            print(f'编号:{index}, 学校名:{school_name}')

        school_choice = input('请输入你要选择的学校名 >>> : ').strip()

        if not school_choice.isdigit():
            print('请输入数字')
            continue
        school_choice = int(school_choice)
        if not school_choice in range(len(re)):
            print('输入的数字超出列表值,请重新输入')
            continue
        school_name = re[school_choice]
        flag, msg = student_interface.student_school_chosen_interface(school_name, student_info.get('user'))
        if flag:
            print(msg)
            break



# 学生选择课程功能
@common.auth('student')
def select_course():
    while True:
        re,msg = common_interface.get_all_school_interface()

        for index, school_name in enumerate(msg):
            print(index, school_name)

        school_choice = input('请输入你要选择的学校名(会返回选择的学校名下的课程列表) >>> : ').strip()

        if not school_choice.isdigit():
            print('请输入数字')
            continue
        school_choice = int(school_choice)
        if not school_choice in range(len(msg)):
            print('输入的数字超出列表值,请重新输入')
            continue
        school_name = msg[school_choice]

        re,msg = student_interface.student_course_choice_interface(school_name,student_info.get('user'))
        if re:
            print(msg)
            break


# 学生查看分数功能
@common.auth('student')
def check_score():
    # 让学生输入校区和课程名

    flag, msg = student_interface.student_check_interface(student_info.get('user'))
    if flag:
        print(msg)
    else:
        print(msg)






func_dict = {
    '1': register,
    '2': login,
    '3': select_school,
    '4': select_course,
    '5': check_score,
}

def student_view():
    while True:
        print(
            '''
            === 欢迎来到管理员系统 ===
                - 1.注册
                - 2.登录
                - 3.选择校区
                - 4.选择课程
                - 5.查看分数
            ===      end      ===
            '''
        )
        choice = input('请选择学生系统的选项进行操作 >>> : ')
        if choice not in func_dict:
            print('没有此选项请重新输入')
            continue

        func_dict[choice]()