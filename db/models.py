# 类的集合处
from db import db_handler


class Base:

    # 因为要先调用save函数,调用db_handler
    def save(self):
        db_handler.save_data(self)

    @classmethod
    def select(cls,user):
        obj = db_handler.select(cls,user)
        return obj


class Admin(Base):
    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd

    def create_school(self,school_name,school_addr):
        sch_obj = School(school_name,school_addr)
        sch_obj.save()

    def create_course(self,school_obj,course_name):
        course_obj = Course(course_name)
        course_obj.save()

        school_obj.course_list.append(course_name)
        school_obj.save()

    def create_teacher(self,teacher_name,pwd):
        teacher_obj = Teacher(teacher_name,pwd)
        teacher_obj.save()


class School(Base):
    def __init__(self,school_name,school_addr):
        self.user = school_name
        self.addr = school_addr
        self.course_list = []


class Course(Base):
    def __init__(self,course_name):
        self.user = course_name
        self.student_list = []

class Teacher(Base):
    def __init__(self,teacher_name,pwd):
        self.user = teacher_name
        self.pwd = pwd
        self.class_choice_list = []

class Student(Base):
    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd
        self.course_chosen_list = []
        self.score = None


