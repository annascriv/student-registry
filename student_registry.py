class Student:
    
    def __init__(self,name="N/A",age=13, grade="12th", subject="N/A"):
        self._name=name
        self._age=age
        self._grade=grade
        self.subject=subject

    @property 
    def get_name(self):
        return self._name
    @get_name.setter
    def set_name(self, new_name):
        if type(new_name) == str and new_name.isalpha() and len(new_name) >= 3 and new_name.title():
            self._name=new_name

    @property 
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if type(new_age) == int and new_age>11 and new_age<18:
            self._age=new_age

    @property
    def get_grade(self):
        return self._grade

    @get_grade.setter
    def set_grade(self, new_grade):
        if 'th' in new_grade and int(new_grade.split('t')[0])<13 and int(new_grade.split('t')[0])>8:
            self._grade=new_grade

    def __str__(self):
        return f"Student 1: Name: {self.get_name}, Age: {self.get_age}, Grade: {self.get_grade}"
    
   # def next_grade(self):
    #    return int(self.grade)+1
    
    def years_advanced(self):
        next_age = int(self.get_grade.split('t')[0])+1
        #print(next_age)
        print(f"{self.get_name} has advanced to the {next_age}th grade")
    
    def study(self):
        print(f"{self.get_name} is studying {self.subject}.")
    
student_one = Student("Anna", 15, '9th', 'Algebra')

student_one.set_name=14
print(student_one)

student_one.set_grade='12th'
print(student_one)



    

