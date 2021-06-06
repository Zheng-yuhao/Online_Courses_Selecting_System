


def auth(role):
    from core import admin,student
    def login_auth(func):
        def inner(*args,**kwargs):
            if role == 'admin':
                if admin.admin_info.get('user'):
                    re = func(*args,**kwargs)
                    return re
                else:
                    admin.login()


            elif role == 'student':
                if student.student_info.get('user'):
                    re = func(*args,**kwargs)
                    return re
                else:
                    student.login()
            #
            # elif role == 'teacher':
            #     if teacher.teacher_info.get('user'):
            #         re = func(*args, **kwargs)
            #         return re
            #     else:
            #         teacher.login()
            else:
                print('当前视图没有权限')

        return inner
    return login_auth

