

class Person(object):

    def __init__(self, name):
        self.name = name
        self.used_skip = False
        self.used_50 = False

        self.correct = 0
        self.total = 0

    def ask_question(self, question, skip_question):
        print()
        print(self.name + " is your turn!")
        question.pretty_print()

        name = None
        while name not in ["A", "B", "C", "D", "SKIP", "50"]:
            name = input("Enter your answer (A, B, C, D, SKIP or 50): ").upper()

            if name in ["A", "B", "C", "D"]:
                if question.is_correct(name):
                    print("Correct!")
                    self.correct += 1
                else:
                    print("Wrong!")

                self.total +=1
            elif name == "SKIP":
                if not self.used_skip:
                    self.used_skip = True

                    self.ask_question(skip_question, None)
                else:
                    print("You cannot skip anymore!")
                    name = None

            elif name == "50":
                if not self.used_50:
                    self.used_50 = True

                    question.pretty_print50()
                    name = None
                else:
                    print("You cannot use 50-50 anymore!")
                    name = None
