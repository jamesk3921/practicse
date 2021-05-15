class stu:
    def __init__(self, age):
        self.age = age

    def cate(self):
        if self.age >= 30:
            return "youth"
        else:
            return "aged"