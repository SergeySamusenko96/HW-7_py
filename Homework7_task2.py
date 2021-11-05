class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_st_for_lect(self, lecturer, course, grade):
        if isinstance (lecturer, Lecturer)and(course in lecturer.courses)and ((course in self.finished_courses)or(course in self.courses_in_progress)):
            if course in lecturer.grades:
               lecturer.grades[course]+=[grade]
            else:
                lecturer.grades[course]=[grade]
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surmane):
        super()._init_(self, name, surname)
        self.courses = []
        self.grades = {}

class Reviewer(Mentor):
    def __init__(self, name, surmane):
        super()._init_(self, name)
        self.courses = []
        
    def rate_rv(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Студент не занимается на данном курсе'

#best_student = Student('Ruoy', 'Eman', 'your_gender')
#best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']


 
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
 
#print(best_student.grades)