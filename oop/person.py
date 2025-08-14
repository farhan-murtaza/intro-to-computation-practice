import datetime

class Person(object):
    
    def __init__(self, name):
        """Create a person"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name 
        self.Birthday = None
    
    def getName(self):
        """Returns self's last name"""
        return self.name
    def getLastName(self):
        """Returns self's last name """
        return self.lastName
    
    def setBirthday(self, birthdate):
        """Assume birthday is of type datetime.date
        Sets self's birthday to birthdate"""
        self.birthday = birthdate
        
    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    
    def __lt__(self, other):
        """Returns True if self precedes other in alphabetical
        order, and False otherwise. Comparison is based on last
        names, but if these are the same full names are
        compared."""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        """Returns self's name"""
        return self.name

me = Person('Michael Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')


class MITPerson(Person):
    
    nextIdNum = 0 # identification number
    
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def isStudent(self):
        return isinstance(self, Student)
        
p1 = MITPerson('Mark Guttag')
p2 = MITPerson('Billy Bob Beaver')
p3 = MITPerson('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')


print('p1 < p2 =', p1 < p2)
print('p3 < p2 =', p3 < p2)
print('p4 < p1 =', p4 < p1)


# Multiple levels of inheritance
class Student(MITPerson):
    pass
class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    
class Grad(Student):
    pass

p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)
print(p5, 'is a graduate student is', type(p5) == Grad)
print(p5, 'is an undergraduate student is', type(p5) == UG)



# check isinstance

print(p5, 'is a student is', p5.isStudent())
print(p6, 'is a student is', p6.isStudent())
print(p3, 'is a student is', p3.isStudent())


class TransferStudent(Student):
    
    def __init__(self, name, fromSchool):
        MITPerson.__init__(self, name)
        self.fromSchool = fromSchool
        
    def getOldSchool(self):
        return self.fromSchool
    

p7 = TransferStudent('John Doe', 'Old School')



# Encapsulation and Information Hiding

class Grades(object):

    def __init__(self):
        """Create an empty grade book"""
        self.sutdents = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """Assume: student is of type Student
        Adds student to the grade book"""
        if student in self.sutdents:
            raise ValueError('Student already exists')
        self.sutdents.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    
    def addGrade(self, student, grade):
        """Assume: grade is a float
        Add grade to the list of grades for student"""

        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in grade book')
        
    def getGrades(self, student):
        """Returns a list of grades for student"""
        try: #return copy of list of student's grades
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in grade book')

    def getStudents(self):
        """Returns a sorted list of the students in the grade book"""
        if not self.isSorted:
            self.sutdents.sort()
            self.isSorted = True
        # return self.sutdents[:]     # return copy of list of students 
        # send a copy of the list is not good practice, so we can use yield generator
        for s in self.sutdents:
            yield s

    
def gradeReport(course):
    """Assumes course is of type Grades"""
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try: 
            average = tot / numGrades
            report = report + '\n'\
                    + str(s) + '\'s mean grade is ' + str(average) 
        except ZeroDivisionError:
            report = report + '\n'\
                    + str(s) + ' has no grades'
            
    return report
    


ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')
sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)
for s in sixHundred.getStudents():
    sixHundred.addGrade(s, 75)
sixHundred.addGrade(g1, 25)
sixHundred.addGrade(g2, 100)
sixHundred.addStudent(ug3)
print(gradeReport(sixHundred))


# Information Hiding 
class infoHiding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsoVisible__ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directly'
    def printVisible(self):
        print(self.visible)
    def printInvisible(self):
        print(self.__invisible)
    def __printInvisible(self):
        print(self.__invisible)
    def __printInvisible__(self):
        print(self.__invisible)

test = infoHiding()
print(test.visible)
print(test.__alsoVisible__)
# print(test.__invisible) # This will raise an AttributeError
test.printInvisible()
test.__printInvisible__()
# test.__printInvisible() # This will raise an AttributeError



