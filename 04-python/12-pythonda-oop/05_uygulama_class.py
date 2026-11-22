# 12.5 Uygulama: Class
# Quiz (sinav) uygulamasi: Question ve Quiz siniflari ile soru-cevap uygulamasi.

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, answer):
        return self.answer.lower() == answer.lower()


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_question(self):
        return self.questions[self.question_index]

    def display_question(self):
        question = self.get_question()
        print(f"\nSoru {self.question_index + 1}: {question.text}")
        for secenek in question.choices:
            print("-" + secenek)
        answer = input("Cevap: ")
        self.guess(answer)
        self.load_question()

    def guess(self, answer):
        question = self.get_question()
        if question.check_answer(answer):
            self.score += 1
        self.question_index += 1

    def load_question(self):
        if len(self.questions) == self.question_index:
            self.show_score()
        else:
            self.display_progress()
            self.display_question()

    def show_score(self):
        print(f"\nSkor: {self.score} / {len(self.questions)}")

    def display_progress(self):
        toplam = len(self.questions)
        print(f"{'*' * 10} Soru {self.question_index + 1} / {toplam} {'*' * 10}")


sorular = [
    Question("En iyi programlama dili hangisidir?",
             ["C#", "Python", "Javascript", "Java"], "Python"),
    Question("En populer programlama dili hangisidir?",
             ["Python", "Javascript", "C#", "Java"], "Python"),
    Question("Python'da liste olusturmak icin hangi parantez kullanilir?",
             ["()", "[]", "{}", "<>"], "[]"),
]

quiz = Quiz(sorular)
quiz.load_question()
