#student1_name = "Aisha"
#student1_gpa = 3.8
 
#student2_name = "Diego"
#student2_gpa = 3.2
 
#def print_student(name, gpa):
 #   print(f"{name}: GPA {gpa}")
 
#print_student(student1_name, student1_gpa)
#print_student(student2_name, student2_gpa)
#s1 = Student('Aisha', 3.8)
#s2 = Student('Diego', 3.2)
#print(s1.name)
#print(s2.name)

class Student:
    def __init__(self, name, gpa):
        self.name = name 
        self.gpa =gpa 

    def setName(self,newName):
        self.name = newName

    def getName(self):
        return self.name
    
    def getGpa(self):
        return self.gpa
    
    def setGpa(self,newGpa):
        if newGpa > 4.0 or newGpa < 0.0:
            print("Invalid new gpa")
        else:
            self.gpa =newGpa

def main():
    s1 =Student('Diego', 3.2)
    s2 = Student('Aisha', 3.8)

    s1.setGpa(5.5) # test bad value
    s1.setGpa(3.0) # test good value

    print(s1.getName())
    print(s1.getGpa())
main()