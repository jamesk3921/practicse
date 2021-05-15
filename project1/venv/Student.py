class Student:
    def __init__(self, name, place, score):
        self.name = name
        self.name = place
        self.score = score

    def passed_exam(self):
        if self.score >= 5:
            print("passed")
        else:
            print("faild")