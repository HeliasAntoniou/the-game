from random import shuffle


class Question(object):

    answer_map = {"A": 0, "B": 1, "C": 2, "D": 3}

    def __init__(self, question, answers):
        assert len(answers) == 4, "Please create questions providing 4 answers"

        self.question = question

        random_shuffle = [0, 1, 2, 3]
        shuffle(random_shuffle)

        self.a1 = "A: " + answers[random_shuffle[0]]
        self.a2 = "B: " + answers[random_shuffle[1]]
        self.a3 = "C: " + answers[random_shuffle[2]]
        self.a4 = "D: " + answers[random_shuffle[3]]

        self.correct_answer = random_shuffle.index(0)

    def is_correct(self, answer):
        answer = Question.answer_map[answer.upper()]

        return answer == self.correct_answer

    def pretty_print(self):
        print(self.question + ": " + ", ".join([self.a1, self.a2, self.a3, self.a4]))

    def pretty_print50(self):
        random_shuffle = [0, 1, 2, 3]
        random_shuffle.remove(self.correct_answer)
        shuffle(random_shuffle)
        wrong = random_shuffle[0]

        answers = [self.a1, self.a2, self.a3, self.a4]
        answers = sorted([answers[wrong], answers[self.correct_answer]])
        print(self.question + ": " + ", ".join(answers))