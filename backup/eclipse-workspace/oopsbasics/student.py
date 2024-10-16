class Student:
    major = "Gem"
    def __init__(self,s):
            self.name=s
    def display(self):
        print(self.major)
            
s1 = Student("shreyas")
print(s1.name)
(s1.display())

s1 = Student("Shweta")
print(s1.name)
(s1.display())
