# 管理员视图层
from interface import admin_interface
from lib import common
from interface import common_interface

admin_info = {
    'user': None
}


def register():
    # 进行简单的用户输入
    print('管理员注册功能正在执行 >>> : ')
    user = input('用户名? >>> : ')
    pwd = input('密码? >>> : ')
    re_pwd = input('再输一次密码? >>> : ')

    if pwd == re_pwd:
        # 如果2次密码校验成功, 调用admin_interface
        flag, msg = admin_interface.admin_register_interface(
            user, pwd
        )
        if flag:
            print(msg)

        else:
            print(msg)


def login():
    while True:
        user = input('请输入用户名 >>> : ')
        pwd = input('请输入密码 >>> : ')
        re_pwd = input('请小伙子再次输入密码 >>> : ')

        if not pwd == re_pwd:
            print('2次密码输入的不对哦')
            continue

        flag, msg = admin_interface.admin_login_interface(user, pwd)
        if flag:
            print(msg)
            admin_info['user'] = user
            break
        else:
            print(msg)


@common.auth('admin')
def create_school():
    while True:
        school_name = input('请输入学校名称 >>> : ')
        school_addr = input('请输入学校地址 >>> : ')

        flag, msg = admin_interface.create_school_interface(school_name, school_addr, admin_info.get('user'))

        if flag:
            print(msg)
            break
        else:
            print(msg)



@common.auth('admin')
def create_course():
    while True:
        # 1.让管理员先选择学校
        # 1.1 调用接口，获取所有学校的名词并打印
        flag, msg = common_interface.get_all_school_interface()
        if not flag:
            print(msg)
            break

        for index, school_name in enumerate(msg):
            print(f'编号:{index}, 学校名:{school_name}')
        choice = input('请输入学校名 >>> : ').strip()

        if not choice.isdigit():
            print('请输入数字类型')
            continue

        choice = int(choice)

        if choice not in range(len(msg)):
            print('超出范围, 请重新输入编号')
            continue
        school_name = msg[choice]
        # 2. 选择学校后，再输入课程名称
        course_name = input('请输入课程名称 >>> : ').strip()
        # 3. 调用创建课程接口, 让管理员去创建课程
        flag, msg = admin_interface.create_course_interface(
            school_name,course_name ,admin_info.get('user')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)

@common.auth('admin')
def create_teacher():
    while True:
        teacher_name = input('请输入教师的名字 >>> : ').strip()
        flag, msg = admin_interface.create_teacher(teacher_name, admin_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)




func_dict = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher,
}


def admin_view():
    while True:
        print(
            '''
            === 欢迎来到管理员系统 ===
                - 1.注册
                - 2.登录
                - 3.创建学校
                - 4.创建课程(先选择学校)
                - 5.创建讲师
            ===      end      ===
            '''
        )
        choice = input('请选择管理员系统的选项进行操作 >>> : ')
        if choice not in func_dict:
            print('没有此选项请重新输入')
            continue

        func_dict[choice]()
