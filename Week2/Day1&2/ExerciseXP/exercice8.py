#Exercise 8 : Star Wars Quiz
"""
Instructions

This project allows users to take a quiz to test their Star Wars knowledge.
The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

Here is an array of dictionaries, containing those questions and answers

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
Create a function that informs the user of his number of correct/incorrect answers.
Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
If he had more then 3 wrong answers, ask him to play again.

"""

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def quiz():
    correct = 0
    incorrect = 0
    wrong_answers = []  
    
    for item in data:
        user_answer = input(item["question"] + " ")  # Pose la question
        if user_answer.strip().lower() == item["answer"].lower():
            print("Correct!\n")
            correct += 1
        else:
            print("Incorrect!\n")
            incorrect += 1
            wrong_answers.append({
                "question": item["question"],
                "your_answer": user_answer,
                "correct_answer": item["answer"]
            })
    return correct, incorrect, wrong_answers

def show_results(correct, incorrect, wrong_answers):
    print("\n----- Quiz Results -----")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}\n")
    
    # Bonus 
    if wrong_answers:
        print("Review of incorrect answers:")
        for item in wrong_answers:
            print(f"Question: {item['question']}")
            print(f"Your answer: {item['your_answer']}")
            print(f"Correct answer: {item['correct_answer']}\n")
    
    if incorrect > 3:
        play_again = input("You got more than 3 questions wrong. Would you like to play again? (yes/no): ")
        if play_again.strip().lower() == "yes":
            main_quiz()  

def main_quiz():
    correct, incorrect, wrong_answers = quiz()
    show_results(correct, incorrect, wrong_answers)

if __name__ == "__main__":
    main_quiz()
