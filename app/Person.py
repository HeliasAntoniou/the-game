

class Person(object):

    def __init__(self, name):
        self.name = name
        self.used_skip = False
        self.used_50 = False

        self.correct = 0
        self.total = 0