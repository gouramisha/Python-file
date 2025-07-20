import tkinter as tk
from tkinter import messagebox

# Sample questions, choices, and answers
questions = [
    "What is the capital of France?",
    "Which language is used for web apps?",
    "What does CPU stand for?",
    "Who developed Python?"
]

choices = [
    ["Paris", "London", "Berlin", "Madrid"],
    ["Python", "Java", "C++", "All of the above"],
    ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Processor Unit"],
    ["Guido van Rossum", "Elon Musk", "Dennis Ritchie", "Mark Zuckerberg"]
]

answers = [0, 3, 1, 0]  # correct options

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.q_no = 0
        self.score = 0
        self.selected_option = tk.IntVar()

        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 16), wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        self.options = []
        for i in range(4):
            radio_btn = tk.Radiobutton(self.root, text="", variable=self.selected_option, value=i, font=("Arial", 14))
            radio_btn.pack(anchor="w")
            self.options.append(radio_btn)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

    def display_question(self):
        self.selected_option.set(-1)
        self.question_label.config(text=questions[self.q_no])
        for i, option in enumerate(choices[self.q_no]):
            self.options[i].config(text=option)

    def next_question(self):
        selected = self.selected_option.get()
        if selected == -1:
            messagebox.showwarning("No selection", "Please select an option")
            return

        if selected == answers[self.q_no]:
            self.score += 1

        self.q_no += 1
        if self.q_no < len(questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        result_text = f"Your Score: {self.score}/{len(questions)}"
        messagebox.showinfo("Quiz Completed", result_text)
        self.root.destroy()

# Run the quiz app
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    app = QuizApp(root)
    root.mainloop()
