class Dance:
    def music(self):
        print("Dance with music")

    def sing(self):
        print("No singing")

class Work:
    def music(self):
        print("No music")
    
    def sing(self):
        print("Can sing at work")

def music_test(student):
    student.music()

latino = Dance()
manager = Work()

music_test(latino)

# полиморфизм в отличии от инкапсуляции позволяет переназначать параментры