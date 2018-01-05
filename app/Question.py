from random import shuffle


class Question(object):

    answer_map = {"A": 0, "B": 1, "C": 2, "D": 3}

    def __init__(self, question, answers):
        assert len(answers) == 4, "Please create questions providing 4 answers"

        self.question = question

        random_shuffle = [0, 1, 2, 3]
        shuffle(random_shuffle)

        self.a1 = answers[random_shuffle[0]]
        self.a2 = answers[random_shuffle[1]]
        self.a3 = answers[random_shuffle[2]]
        self.a4 = answers[random_shuffle[3]]

        self.correct_answer = random_shuffle.index(0)

    def is_correct(self, answer):
        answer = Question.answer_map[answer.upper()]

        return answer == self.correct_answer

    def pretty_print(self):
        print(self.question + ": " + ", ".join(["A: " + self.a1, "B: " + self.a2, "C: " + self.a3, "D: " + self.a4]))

    def pretty_print50(self):
        print("TODO")
