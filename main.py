class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def ever_grade(self):
        res=0
        for k,v in self.grades.items():
            res+=sum(v)/len(v)
        return res/len(self.grades)

    def __str__(self):
        return  f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' \
                f'Средняя оценка за лекции: {self.ever_grade()}\n'\
                f'Курсы в процессе изучения:{",".join(self.courses_in_progress)}\n' \
                f'Завершенные курсы: {", ".join(self.finished_courses)}'
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __lt__(self, other):
          return self.ever_grade()<other.ever_grade()
    def __le__(self, other):
          return self.ever_grade()<=other.ever_grade()
    def __eq__(self, other):
          return self.ever_grade()==other.ever_grade()
    def __ne__(self, other):
          return self.ever_grade()!=other.ever_grade()
    def __gt__(self, other):
          return self.ever_grade()>other.ever_grade()
    def __ge__(self, other):
          return self.ever_grade()>=other.ever_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def ever_grade(self):
        res=0
        for k,v in self.grades.items():
            res+=sum(v)/len(v)
        return res/len(self.grades)

    def __str__(self):
        return  f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {self.ever_grade()}\n'
    def __lt__(self, other):
          return self.ever_grade()<other.ever_grade()
    def __le__(self, other):
          return self.ever_grade()<=other.ever_grade()
    def __eq__(self, other):
          return self.ever_grade()==other.ever_grade()
    def __ne__(self, other):
          return self.ever_grade()!=other.ever_grade()
    def __gt__(self, other):
          return self.ever_grade()>other.ever_grade()
    def __ge__(self, other):
          return self.ever_grade()>=other.ever_grade()
class Reviewer(Mentor):
    def __str__(self):
        return  f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n'
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def ever_student(students,name_course):
    res=0
    val=0
    for st in students:
        if name_course in st.courses_in_progress:
            res+=st.ever_grade()
            val+=1
    return res/val

def ever_lecture(lectures,name_course):
    res=0
    val=0
    for le in lectures:
        if name_course in le.courses_attached:
            res+=le.ever_grade()
            val+=1
    return res/val

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']

cool_Reviewer.rate_hw(best_student, 'Python', 7)
cool_Reviewer.rate_hw(best_student, 'Python', 7)
cool_Reviewer.rate_hw(best_student, 'Python', 7)

print('Оценки студента: ', best_student.grades)


cool_Lecturer=Lecturer('Name1', 'Surname2')
cool_Lecturer.courses_attached += ['Python']

best_student.rate_hw(cool_Lecturer, 'Python', 8)
best_student.rate_hw(cool_Lecturer, 'Python', 7)
best_student.rate_hw(cool_Lecturer, 'Python', 6)
print('Оценки лектора: ', cool_Lecturer.grades)

print()
print('Замена str reviewer:')
print(cool_Reviewer)

print('Замена str лектор:')
print(cool_Lecturer)

print('Замена str student:')
print(best_student)

student1 = Student('Name1', 'Surname1', 'male')
student1.courses_in_progress += ['Python']
student2 = Student('Name2', 'Surname2', 'male')
student2.courses_in_progress += ['SQL']

cool_Reviewer.rate_hw(student1, 'Python', 7)
cool_Reviewer.rate_hw(student1, 'Python', 5)
cool_Reviewer.rate_hw(student2, 'SQL', 7)
cool_Reviewer.rate_hw(student2, 'SQL', 8)

cool_Lecturer2=Lecturer('Name2', 'Surname2')
cool_Lecturer2.courses_attached += ['Python']

cool_Lecturer3=Lecturer('Name3', 'Surname3')
cool_Lecturer3.courses_attached += ['SQL']

student1.rate_hw(cool_Lecturer2, 'Python', 9)
student1.rate_hw(cool_Lecturer2, 'Python', 8)

student2.rate_hw(cool_Lecturer3, 'SQL', 9)
student2.rate_hw(cool_Lecturer3, 'SQL', 9)

students_1=[]
students_1.append(best_student)
students_1.append(student1)
students_1.append(student2)

print(ever_student(students_1,'Python'))

lectures_1=[]
lectures_1.append(cool_Lecturer)
lectures_1.append(cool_Lecturer2)
lectures_1.append(cool_Lecturer3)

print(ever_lecture(lectures_1,'Python'))