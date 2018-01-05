from app.Person import Person
from app.Questions import Questions


if __name__ == "__main__":

    persons = [Person("Spyridoyla"), Person("Helias"), Person("Anastasia")]

    questions = Questions()

    for q in questions.ques:
        for p in persons:
            p.ask_question(q, questions.skip)
