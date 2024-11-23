import tkinter as tk
from tkinter import messagebox
import time
import random

# Sample quiz questions
quiz_questions_easy = {
    "General Programming": [
        {"question": "What is 2 + 2?", "options": ["A) 3", "B) 4", "C) 5", "D) 6"], "answer": "B"},
        {"question": "What is the output of print(5 + 5)?", "options": ["A) 10", "B) 55", "C) 5", "D) 50"], "answer": "A"},
    ]
}

# Function to get valid input (only A, B, C, D)
def get_valid_answer(answer):
    valid_answers = ['A', 'B', 'C', 'D']
    if answer in valid_answers:
        return answer
    else:
        return None

# Main window for the quiz
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        self.score = 0
        self.total_questions = 0
        self.current_question = 0
        self.time_limit = 10  # 10 seconds per question
        self.start_time = None
        
        # Quiz question categories
        self.questions = quiz_questions_easy
        
        self.create_main_menu()

    def create_main_menu(self):
        # Main menu screen
        self.clear_window()
        
        self.title_label = tk.Label(self.root, text="Welcome to the Quiz Game", font=("Arial", 24))
        self.title_label.pack(pady=20)
        
        self.start_button = tk.Button(self.root, text="Start Quiz", font=("Arial", 16), command=self.start_quiz)
        self.start_button.pack(pady=10)
        
        self.high_scores_button = tk.Button(self.root, text="View High Scores", font=("Arial", 16), command=self.view_high_scores)
        self.high_scores_button.pack(pady=10)
        
        self.quit_button = tk.Button(self.root, text="Quit", font=("Arial", 16), command=self.root.quit)
        self.quit_button.pack(pady=10)

    def start_quiz(self):
        # Start quiz screen
        self.clear_window()
        
        self.score = 0
        self.total_questions = 0
        self.current_question = 0
        self.show_question()

    def show_question(self):
        # Display the question and options
        question_data = self.questions["General Programming"][self.current_question]
        question = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["answer"]
        
        self.title_label = tk.Label(self.root, text=question, font=("Arial", 18))
        self.title_label.pack(pady=20)

        # Timer display
        self.timer_label = tk.Label(self.root, text=f"Time left: {self.time_limit} seconds", font=("Arial", 14))
        self.timer_label.pack(pady=10)

        self.option_buttons = []
        for option in options:
            button = tk.Button(self.root, text=option, font=("Arial", 14), command=lambda option=option: self.check_answer(option, correct_answer))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.start_time = time.time()
        self.update_timer()

    def check_answer(self, user_answer, correct_answer):
        # Check if the answer is correct
        if user_answer[0] == correct_answer:
            self.score += 1
        
        self.total_questions += 1
        self.current_question += 1

        if self.current_question < len(self.questions["General Programming"]):
            self.show_question()
        else:
            self.end_quiz()

    def update_timer(self):
        # Update the timer countdown
        elapsed_time = int(time.time() - self.start_time)
        time_left = self.time_limit - elapsed_time
        if time_left >= 0:
            self.timer_label.config(text=f"Time left: {time_left} seconds")
            self.root.after(1000, self.update_timer)
        else:
            self.check_answer('E', 'E')  # Automatically mark it wrong if time is up

    def end_quiz(self):
        # End of quiz, show score
        self.clear_window()
        
        self.title_label = tk.Label(self.root, text=f"Quiz Finished!\nYour score: {self.score}/{self.total_questions}", font=("Arial", 18))
        self.title_label.pack(pady=20)
        
        self.save_score_button = tk.Button(self.root, text="Save Score", font=("Arial", 14), command=self.save_score)
        self.save_score_button.pack(pady=10)
        
        self.main_menu_button = tk.Button(self.root, text="Back to Main Menu", font=("Arial", 14), command=self.create_main_menu)
        self.main_menu_button.pack(pady=10)

    def save_score(self):
        user_name = "Player"  # Replace with user input if desired
        with open("high_scores.txt", "a") as file:
            file.write(f"{user_name}: {self.score}\n")
        messagebox.showinfo("Score Saved", f"Your score has been saved!")

    def view_high_scores(self):
        # View high scores
        self.clear_window()
        
        try:
            with open("high_scores.txt", "r") as file:
                scores = file.readlines()
        except FileNotFoundError:
            scores = []

        self.title_label = tk.Label(self.root, text="High Scores", font=("Arial", 24))
        self.title_label.pack(pady=20)

        if scores:
            for score in scores:
                score_label = tk.Label(self.root, text=score.strip(), font=("Arial", 16))
                score_label.pack()
        else:
            self.no_scores_label = tk.Label(self.root, text="No high scores yet.", font=("Arial", 16))
            self.no_scores_label.pack(pady=20)
        
        self.main_menu_button = tk.Button(self.root, text="Back to Main Menu", font=("Arial", 14), command=self.create_main_menu)
        self.main_menu_button.pack(pady=10)

    def clear_window(self):
        # Clear the window to prepare for the next screen
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
