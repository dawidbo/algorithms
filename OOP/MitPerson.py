class Person(object):
    
    def __init__(self, fname):
        self.name = fname

    def __str__(self):
        return self.name
        
class MITPerson(Person):
    id = 0
    def __init__(self, fname):
        Person.__init__(self,fname)
        self.idNum  =MITPerson.id
        MITPerson.id += 1    
    def __lt__(self, other):
        return self.idNum < other.idNum
    # def __str__(self):
     # return self.name
    def getID(self):
        return self.idNum 

m3 = MITPerson("oleg")
m2 = MITPerson("eric")
m1 = MITPerson("ass")
m0 = Person("john")

MitList = [m1,m2,m3]

for e in MitList:
    print(e)

print()

MitList.sort()
for e in MitList:
    print(e.getID())
    print(e)

#print( m3.__lt__(m0))

#  !!! shadowing 
class Grades(object):
    """mapping from students to list of grades"""
    def __init__(self):
        """ Create empty grade book """
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """ Assusme: Student is of type Student
            Add studend to Grade Book"""
        if student in self.students:
            raise ValueError("Duplicates Students")
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrades(self, student, grade):
        """Assume: greade is float
        Add grade to the list of grades for students"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError("Student not in grade book")

    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]
        #return a copy of list of students
    
    def allStudents1(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s

def gradeReport(course):
    """course is type of grade """
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot / numGrades
            report.append(str(s) + '\' mean grade is ' + str(average) + "\n")
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades \n ')
    return ''.join(report)


class Student(object):
    id = 0
    def __init__(self, fname, fyear):
        self.name = fname
        self.year = fyear
        self.IdNum = Student.id
        Student.id += 1
    def getIdNum(self):
        return self.IdNum    
    def getName(self):
        return self.name
    def __str__(self):
        return str(self.name)
    def __lt__(self, other):
        if self.IdNum < other.IdNum:
            return self.IdNum
        return other.IdNum

ug1 = Student("mat damon", 2018)
ug2 = Student("ben affleck", 2018)
ug3 = Student("bill gates", 2017)


six00 = Grades()
six00.addStudent(ug1) 
six00.addStudent(ug2) 
six00.addStudent(ug3)

for e in six00.allStudents():
    print(e)



six00.addGrades(ug1, 1.0)
six00.addGrades(ug1, 1.0)

six00.addGrades(ug2, 2.0)
six00.addGrades(ug2, 2.0)

six00.addGrades(ug3, 3.0)
six00.addGrades(ug3, 3.0)


print(gradeReport(six00))

for e in six00.allStudents():
    print(e)