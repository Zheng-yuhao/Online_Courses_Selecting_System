from core import admin
from core import student
from core import teacher

func_dict = {
    '1':admin.admin_view,
    '2':student.student_view,
    '3':None
}

def run():
    while True:
        print(
            '''
            === 欢迎来到选课系统 ===
                1. 管理员功能
                2. 学生功能
                3. 老师功能
            ===      end      ===
            '''
        )

        choice = input('请选择你想要进入的功能选项 >>> : ').strip()
        if choice not in func_dict:
            print('没有此选项,请重新选择')
            continue
        func_dict[choice]()