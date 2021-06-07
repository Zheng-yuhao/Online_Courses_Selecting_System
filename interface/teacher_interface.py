from db import models


# Teacher's login interface function
def teacher_login_interface(user, pwd):
    # check the user_id by import models.Teacher which has been arranged by necessary functions
    re = models.Teacher.select(user)

    # If has the obj of teacher, return True
    if re:
        return True, f'User_id {[user]} login is successful'

    # If not, return False
    teacher_obj = models.Teacher(user, pwd)
    teacher_obj.save()
    return False, f'There is no data of {user}, please contact admin to help you creating a new teacher account.'


# Teacher's checking interface
def teacher_check_list_interface(user):
    teacher_obj = models.Teacher.select(user)
    if teacher_obj:
        return True, teacher_obj.class_choice_list
    return False, f'Theres are no data in user{[user]}\'s course_list, please select your class first. '


# Teacher's course selection interface
def teacher_select_course_interface(course_name, user):
    teacher_obj = models.Teacher.select(user)
    teacher_obj.class_choice_list.append(course_name)
    teacher_obj.save()
    return True, f'User{[user]}, course_name{[course_name]},selection successful.'


# Teacher's checking student interface
def teacher_check_student_interface(course_name):
    course_obj = models.Course.select(course_name)
    return True, course_obj.student_list
