class student:
    grade = 10
    name = "DEV supreme"
    def introduction(self):
        print("Hi im am a Developer")

    def details(self):
        print("My name is ",self.name," and I am at grade", self.grade)

ob = student()
ob.introduction()
ob.details()