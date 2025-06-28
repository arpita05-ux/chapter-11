class Number:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)

x = Number(100)
print(x.__str__())        # or also write as print(str(x))


#another example

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # ← this gets called by print(s)
        return f"{self.name}, {self.age}"

s = Student("Arpita", 18)

# Another example

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # ← this gets called by print(s)
        return f"{self.name}, {self.age}"

s = Student("Arpita", 18)

print(s)  # 👈 Calls s.__str__() → prints "Arpita, 18"
