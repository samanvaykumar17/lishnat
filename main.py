import random

from kivy.app import App
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout


class QuizScreen(BoxLayout):
    score = NumericProperty(0)
    question_text = StringProperty("")
    status_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total_questions = 10
        self.current_question = 0
        self.a = 0
        self.b = 0
        self.next_question()

    def next_question(self):
        self.a = random.randint(2, 9)
        self.b = random.randint(2, 9)

        self.question_text = (
            f"Question {self.current_question + 1}/{self.total_questions}\n"
            f"{self.a} × {self.b} = ?"
        )

        self.ids.answer_input.text = ""

    # ---------- Number Pad ----------
    def add_digit(self, digit):
        self.ids.answer_input.text += str(digit)

    def backspace(self):
        self.ids.answer_input.text = self.ids.answer_input.text[:-1]

    def clear_answer(self):
        self.ids.answer_input.text = ""

    # ---------- Submit ----------
    def submit_answer(self):
        answer = self.ids.answer_input.text.strip()

        try:
            if int(answer) == self.a * self.b:
                self.score += 1
                self.status_text = "✅ Correct!"
            else:
                self.status_text = f"❌ Wrong! Answer = {self.a * self.b}"
        except ValueError:
            self.status_text = "Enter an answer."
            return

        if self.current_question < self.total_questions - 1:
            self.current_question += 1
            self.next_question()
        else:
            self.show_result()

    def show_result(self):
        self.question_text = f"Quiz Finished!\n\nScore: {self.score}/10"

        if self.score == 10:
            self.status_text = "🎉 You Win!"
        else:
            self.status_text = "Press Play Again"

        self.ids.submit_btn.disabled = True
        self.ids.play_again_btn.disabled = False

    def reset_game(self):
        self.score = 0
        self.current_question = 0
        self.status_text = ""

        self.ids.submit_btn.disabled = False
        self.ids.play_again_btn.disabled = True

        self.next_question()


class MultiplicationApp(App):
    def build(self):
        return QuizScreen()


if __name__ == "__main__":
    MultiplicationApp().run()
