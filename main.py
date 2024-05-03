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

