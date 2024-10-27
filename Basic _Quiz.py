
def display_question(question, options):
    print(question)
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")

def get_user_input(num_options):
    while True:
        try:
            answer = int(input("Your answer (1-{}): ".format(num_options)))
            if 1 <= answer <= num_options:
                return answer
            else:
                print("Invalid input. Please select a number between 1 and {}.".format(num_options))
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def main():
    questions = [
        {"question": "python program is saved with extention?", "options": [".py", ".phy", ".python"], "answer": 1},
        {"question": "Which planet is known as the Blue Planet?", "options": ["Earth", "Mars", "Jupiter"], "answer": 1},
        {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Pacific"], "answer": 3}
    ]

    score = 0

    for q in questions:
        display_question(q["question"], q["options"])
        user_answer = get_user_input(len(q["options"]))
        if check_answer(user_answer, q["answer"]):
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is: {}".format(q["options"][q["answer"] - 1]))
    
    print("Your final score is {}/{}".format(score, len(questions)))

if __name__ == "__main__":
    main()
