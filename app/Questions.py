from app.Question import Question


class Questions(object):

    def __init__(self):
        self.ques = [Question("What is the second largest island in Greece?", ["Evia", "Crete", "Rodes", "Samos"]),
                     Question("What is the largest greek football club?", ["Olympiacos", "Vazelos",
                                                                           "Chanoumi", "Mpougatses"]),
                     Question("What is Einstain first name?", ["Albert", "John", "Mike", "Steven"])]

        self.skip = Question("What is larger?", ["1", "-1", "0", "0.999"])