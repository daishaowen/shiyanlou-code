#!/usr/bin/env python3
import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self):
        return

class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, grade, branch, year):
        Person.__init__(self, name, grade)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
        grades = Counter(self.grade)
        passes = grades['A'] +grades['B'] + grades['C']
        failes = grades['D']
        return "Pass:{}, Fail:{}".format(passes,failes)


class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, grade, papers):
        Person.__init__(self, name, grade)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        grades = Counter(self.grade)
        return "A:{}, B:{}, C:{}, D{}".format(grades['A'],grades['B'],grades['C'],grades['D'])

person1 = Person('Sachin', sys.argv[2])
student1 = Student('Kushal', sys.argv[2], 'CSE', 2005)
teacher1 = Teacher('Prashad', sys.argv[2], ['C', 'C++'])

if sys.argv[1] == "student":
    #print(person1.get_details())
    #print(student1.get_details())
    print(student1.get_grade())
else:
    #print(teacher1.get_details())
    print(teacher1.get_grade())
