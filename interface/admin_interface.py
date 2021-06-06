# 管理层实际逻辑层
from db import models



def admin_register_interface(user, pwd):
    # 调用select函数,简单用户名或者说用户的文件存不存在
    admin_obj = models.Admin(user, pwd)
    re = admin_obj.select(user)
    if re:
        return False, f'管理员用户{user}已存在,无法重复注册'

    admin_obj.save()
    return True, f'因管理员id不存在,用户名{user}的管理员权限创建成功'



def admin_login_interface(user,pwd):
    admin_obj = models.Admin(user,pwd)
    if pwd == admin_obj.pwd:

        return True, f'管理员用户名{user}登录成功'
    return False, f'管理员用户名{user}未找到,请重新登录尝试'



def create_school_interface(school_name,school_addr,admin_id):
    # 第一步, 先检查有没有当前的学校名和学校地址
    sch_obj = models.School.select(school_name)
    # 第二步, 如果有的话返回False, '学校已存在'
    if sch_obj:
        return False, f'学校名{school_name}已经存在请重新输入'

    # 第三步, 如果没有的话调用save函数,并且返回True, '学校创建成功'
    admin_obj = models.Admin.select(admin_id)
    admin_obj.create_school(school_name,school_addr)
    return True, f'学校名{school_name}创建成功'



def create_course_interface(school_name,course_name,admin_name):
    # 检查传入的course_name是否存在School类中的School_name的course_list中
    school_obj = models.School.select(school_name)
    print(school_obj.__dict__)
    if course_name in school_obj.course_list:
        return False, f'课程{course_name}已存在'
    # 如果不存在的话
    #  先生成admin的对象, 用admin去创建课程
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(school_obj,course_name)
    return True, f'课程{course_name}创建成功,本次创建由admin{admin_name}创建, 并且与学校{school_name}绑定'



def create_teacher(teacher_name,admin_name,pwd=123):
    # 先判断老师是否存在
    teacher_obj = models.Teacher.select(teacher_name)
    if teacher_obj:
        return False, f'老师{teacher_name}已存在,无法继续注册'

    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name,pwd)
    return True, f'老师{teacher_name}创建成功'
