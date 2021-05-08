class School:
    def __init__(self, location, students):
        self.location = "Kyrgyzstan"
        self.students = 1000

class regionSchool(School):
    def director(self):
        return self.location

print(School)

# наследование посзволяет давать объекту единые параметры, которые позже можно заново не определять