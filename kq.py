import time
import random
from PIL import Image

# Dictionary to store the quiz questions and answers
quiz_questions_easy = {
    "General Programming": [
        {"question": "What is 2 + 2?", "options": ["A) 3", "B) 4", "C) 5", "D) 6"], "answer": "B"},
        {"question": "What is the output of print(5 + 5)?", "options": ["A) 10", "B) 55", "C) 5", "D) 50"], "answer": "A"},
        {"question": "What is the value of 3 * 3?", "options": ["A) 6", "B) 9", "C) 12", "D) 15"], "answer": "B"},
        {"question": "Which of the following is a Python library for data manipulation?", "options": ["A) NumPy", "B) Pandas", "C) Matplotlib", "D) All of the above"], "answer": "D"},
        {"question": "What is the result of print(2 ** 3)?", "options": ["A) 5", "B) 8", "C) 9", "D) 6"], "answer": "B"},
        # Add more easy questions here (10 total)
    ],
    "Amplitude and Signal Processing": [
        {"question": "What does the term 'amplitude' refer to in signal processing?", "options": ["A) Frequency of the signal", "B) The height of the wave", "C) The duration of the signal", "D) The phase of the signal"], "answer": "B"},
        {"question": "What is the Nyquist theorem related to?", "options": ["A) Signal modulation", "B) Sampling frequency", "C) Signal attenuation", "D) Noise reduction"], "answer": "B"},
        {"question": "What is Fourier Transform used for?", "options": ["A) Signal analysis", "B) Signal filtering", "C) Compression", "D) Noise reduction"], "answer": "A"},
        {"question": "In digital signal processing, what is sampling?", "options": ["A) Converting analog signals to digital form", "B) Filtering a signal", "C) Modulating a signal", "D) Amplifying a signal"], "answer": "A"},
        {"question": "Which is used to measure the bandwidth of a signal?", "options": ["A) Frequency", "B) Amplitude", "C) Phase", "D) Time"], "answer": "A"},
        # Add more amplitude and signal questions here (10 total)
    ]
}

quiz_questions_medium = {
    "General Programming": [
        {"question": "What is the output of the following code? print(type(5))", "options": ["A) <class 'int'>", "B) <class 'str'>", "C) <class 'float'>", "D) <class 'list'>"], "answer": "A"},
        {"question": "Which of the following is a mutable data type in Python?", "options": ["A) Tuple", "B) String", "C) List", "D) Integer"], "answer": "C"},
        {"question": "Which of the following is not a valid variable name in Python?", "options": ["A) 1st_variable", "B) variable_1", "C) variable-1", "D) variable.1"], "answer": "C"},
        {"question": "What is the purpose of the break statement in loops?", "options": ["A) To skip the current iteration", "B) To exit the loop", "C) To pause the loop", "D) To continue the loop"], "answer": "B"},
        {"question": "What is the purpose of the return statement in a function?", "options": ["A) To end the function", "B) To return a value from the function", "C) To call another function", "D) To print a value"], "answer": "B"},
        # Add more medium difficulty questions here (20 total)
    ],
    "Data Manipulation and Web Technologies": [
        {"question": "What does HTML stand for?", "options": ["A) Hyper Text Markup Language", "B) Hyperlinks and Text Markup Language", "C) High-Level Text Markup Language", "D) Hyper Text Management Language"], "answer": "A"},
        {"question": "Which of the following is a Python web framework?", "options": ["A) Django", "B) Flask", "C) Ruby on Rails", "D) Both A and B"], "answer": "D"},
        {"question": "What is the correct way to declare a variable in JavaScript?", "options": ["A) var", "B) let", "C) const", "D) All of the above"], "answer": "D"},
        {"question": "What is the output of console.log(1 + '1') in JavaScript?", "options": ["A) 2", "B) '11'", "C) '2'", "D) 11"], "answer": "B"},
        {"question": "Which of the following is a NoSQL database?", "options": ["A) MySQL", "B) PostgreSQL", "C) MongoDB", "D) SQLite"], "answer": "C"},
        # Add more web and data manipulation questions here (10 total)
    ]
}

quiz_questions_hard = {
    "General Programming": [
        {"question": "Which of the following is not a programming language?", "options": ["A) Python", "B) Java", "C) HTML", "D) C++"], "answer": "C"},
        {"question": "What is the time complexity of accessing an element in an array?", "options": ["A) O(n)", "B) O(log n)", "C) O(1)", "D) O(n^2)"], "answer": "C"},
        {"question": "Which of the following sorting algorithms has the best average-case time complexity?", "options": ["A) Bubble Sort", "B) Selection Sort", "C) Quick Sort", "D) Insertion Sort"], "answer": "C"},
        {"question": "In Java, what is the default value of an integer variable?", "options": ["A) 0", "B) 1", "C) null", "D) undefined"], "answer": "A"},
        {"question": "What is the primary purpose of the return statement in a function?", "options": ["A) To end the function", "B) To return a value from the function", "C) To call another function", "D) To print a value"], "answer": "B"},
        # Add more hard questions here (10 total)
    ],
    "Advanced Data and Algorithms": [
        {"question": "What is the difference between merge sort and quicksort?", "options": ["A) Merge sort is a divide-and-conquer algorithm, Quick sort is not", "B) Quick sort is always faster than merge sort", "C) Merge sort is stable, quicksort is not", "D) Both A and B"], "answer": "C"},
        {"question": "Which of the following data structures is used for implementing recursion?", "options": ["A) Stack", "B) Queue", "C) Array", "D) Linked List"], "answer": "A"},
        {"question": "What is a deadlock in computer science?", "options": ["A) When a program crashes", "B) When two processes are stuck in a waiting state", "C) When a process takes too long to complete", "D) When memory is unavailable"], "answer": "B"},
        {"question": "Which of the following is a property of a binary tree?", "options": ["A) Each node has at most two children", "B) Each node has exactly two children", "C) Binary trees are always balanced", "D) All nodes are connected in a cycle"], "answer": "A"},
        {"question": "What is the time complexity of binary search?", "options": ["A) O(n)", "B) O(log n)", "C) O(n^2)", "D) O(1)"], "answer": "B"},
        # Add more advanced data and algorithm questions here (10 total)
    ]
}

# Function to get valid input (only A, B, C, D)
def get_valid_answer():
    valid_answers = ['A', 'B', 'C', 'D']
    while True:
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if answer in valid_answers:
            return answer
        else:
            print("Invalid input! Please enter A, B, C, or D.")

# Function to ask questions with timer
def ask_question_with_timer(question, options, correct_answer):
    time_limit = 10  # 10 seconds to answer
    print(f"\n{question}")
    for option in options:
        print(option)
    
    start_time = time.time()  # Record the start time
    while time.time() - start_time < time_limit:
        answer = input(f"You have {time_limit - int(time.time() - start_time)} seconds left: ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            break
    else:
        print("\nTime's up!")
        answer = 'E'  # Assign a wrong answer if time is up
    return answer == correct_answer

# Function to shuffle quiz questions and answers
def shuffle_quiz(questions):
    for category, question_set in questions.items():
        random.shuffle(question_set)
        for q in question_set:
            random.shuffle(q["options"])

# Function to run the quiz game
def run_quiz(questions, time_limit=300):
    start_time = time.time()
    score = 0
    total_questions = 0

    # Shuffle questions and options
    shuffle_quiz(questions)

    # Loop through each category of questions
    for category, question_set in questions.items():
        if time.time() - start_time > time_limit:
            print("\nTime's up! Quiz ended.")
            break
        print(f"\nCategory: {category}")
        
        # Loop through each question in the category
        for q in question_set:
            if time.time() - start_time > time_limit:
                print("\nTime's up! Quiz ended.")
                break
            print(f"\n{q['question']}")
            
            for option in q["options"]:
                print(option)
            
            answer = get_valid_answer()
            
            if answer == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {q['answer']}.")
            
            total_questions += 1

    print(f"\nQuiz completed! Your final score is {score}/{total_questions}.")

# Save the user's score
def save_score(user_name, score):
    with open("high_scores.txt", "a") as file:
        file.write(f"{user_name}: {score}\n")
    print(f"Score saved! {user_name}: {score}")

# Show the high scores
def view_high_scores():
    with open("high_scores.txt", "r") as file:
        scores = file.readlines()
        if scores:
            print("\nHigh Scores:")
            for score in scores:
                print(score.strip())
        else:
            print("No high scores yet!")

# Main Menu
def show_menu():
    print("\n--- Main Menu ---")
    print("1. Start Quiz")
    print("2. View High Scores")
    print("3. Quit")

# Display image (if applicable)
def display_image(image_path):
    img = Image.open(image_path)
    img.show()

# Main game function
def main():
    user_name = input("Enter your name: ")
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            difficulty = input("Choose difficulty (Easy/Medium/Hard): ").lower()
            if difficulty == 'easy':
                run_quiz(quiz_questions_easy)
            elif difficulty == 'medium':
                run_quiz(quiz_questions_medium)
            elif difficulty == 'hard':
                run_quiz(quiz_questions_hard)
            save_score(user_name, score)
        elif choice == '2':
            view_high_scores()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
