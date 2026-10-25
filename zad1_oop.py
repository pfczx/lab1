class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks = marks

    def is_passed(self):
        if sum(self.marks)/len(self.marks) > 0.5 * len(self.marks):
            return True
        else:
            return False

s1 = Student("s1",[1,1,1,3,2])
s2 = Student ("s2",[5,3])

print(s1.is_passed())
print(s2.is_passed())
