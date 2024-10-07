from group import Group
from people.student import Student
from abc import abstractmethod

class CourseAB():
    def __init(self,name:str):
        self.name = name
        self.groups :list[Group] =[]

    @abstractmethod
    def register_student(self,student:Student):
        pass
    
    def add_group(self, group:Group):
        if group and group not in self.groups:
            self.groups.append(group)
    



