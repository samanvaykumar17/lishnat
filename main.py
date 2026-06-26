import random

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout


class QuizScreen(BoxLayout):
    score = NumericProperty(0)
    question_text = StringProperty("")
    status_text = StringProperty("")
    time_text = StringProperty("00.0")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.total_questions = 10
        self.current_question = 0

        self.a = 0
        self.b = 0

        self.elapsed = 0.0

        Clock.schedule_interval(self.update_timer, 0.1)

        self.next_question()

    # ---------------- Timer ----------------

    def update_timer(self, dt):
        self.elapsed += dt

        minutes = int(self.elapsed // 60)
        seconds = self.elapsed % 60

        self.time_text = f"{minutes:02d}:{seconds:04.1f}"

    # ---------------- Questions ----------------

    def next_question(self):
        self.a = random.randint(2, 9)
        self.b = random.randint(2, 9)

        self.question_text = (
            f"Question {self.current_question + 1}/{self.total_questions}\n"
            f"{self.a} × {self.b} = ?"
        )

        self.ids.answer_input.text = ""

    # ---------------- Keypad ----------------

    def add_digit(self, digit):
        self.ids.answer_input.text += str(digit)

    def backspace(self):
        self.ids.answer_input.text = self.ids.answer_input.text[:-1]

    def clear_answer(self):
        self.ids.answer_input.text = ""

    # ---------------- Submit ----------------

    def submit_answer(self):

        txt = self.ids.answer_input.text.strip()

        if txt == "":
            return

        if int(txt) == self.a * self.b:
            self.score += 1
            self.status_text = "✅ Correct"
        else:
            self.status_text = f"❌ {self.a} × {self.b} = {self.a*self.b}"

        if self.current_question < self.total_questions - 1:
            self.current_question += 1
            self.next_question()
        else:
            self.show_result()

    # ---------------- Finish ----------------

    def show_result(self):

        Clock.unschedule(self.update_timer)

        self.question_text = (
            "Quiz Finished!\n\n"
            f"Score : {self.score}/10\n"
            f"Time : {self.time_text}"
        )

        if self.score == 10:
            self.status_text = "🎉 YOU WIN!"
        else:
            self.status_text = "Tap Play Again"

        self.ids.submit_btn.disabled = True
        self.ids.play_again_btn.disabled = False

    # ---------------- Restart ----------------

    def reset_game(self):

        self.score = 0
        self.current_question = 0

        self.elapsed = 0
        self.time_text = "00:00.0"

        self.status_text = ""

        self.ids.submit_btn.disabled = False
        self.ids.play_again_btn.disabled = True

        Clock.unschedule(self.update_timer)
        Clock.schedule_interval(self.update_timer, 0.1)

        self.next_question()


class MultiplicationApp(App):
    def build(self):
        return QuizScreen()


if __name__ == "__main__":
    MultiplicationApp().run()
