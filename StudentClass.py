class Student:
    Name='Unknown'
    Age='Unknown'
    Grade='Unknown'
    School='Unknown'
    Subjects=['Math','Science','Humanities','P.E.','Drama']
    def __init__(self,name,age,grade,school):
        self.Name=name
        self.Age=age
        self.Grade=grade
        self.School=school
    def IsOlder(self,age):
        if self.Age>age:
            return True
        else:
            return False
    def IsStudying(self,Subject):
        if self.Subjects.count(Subject)==0:
            return False
        else:
            return True
