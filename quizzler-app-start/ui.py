from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox



THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, font=("Arial", 15, "italic"),
                                                     fill=THEME_COLOR, text="Some Question",width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(column=1, row=2)
        true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")
            messagebox.showinfo(title="Game completed!",
                                message=f"You've completed the quiz!\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")

    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_clicked(self):
            is_right = self.quiz.check_answer("False")
            self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
            self.score.config(text=f"score: {self.quiz.score}")
        elif is_right == False:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




