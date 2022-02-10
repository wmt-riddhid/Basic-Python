class student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age 
        self.grades = grades
s1 = student("abc", 19, "A+")
s2 = student("pqr", 21, "B")
s3 = student("xyz", 21, "A")

print(s1.name)
print(s1.age)
print(s1.grades)

print(s2.name)
print(s2.age)
print(s2.grades)

print(s3.name)
print(s3.age)
print(s3.grades)