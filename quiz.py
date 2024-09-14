def quiz_game():
    questions = {
        "What is the capital of France?": "Paris",
        "Who wrote 'Hamlet'?": "Shakespeare",
        "What is 5 + 7?": "12",
        "What is the largest ocean on Earth?": "Pacific"
    "Who is the first man on the moon?" : "Neil Armstrong"
    }
    
    score = 0
    
    for question, answer in questions.items():
        user_answer = input(f"{question} ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")
    
    print(f"\nYour final score is: {score}/{len(questions)}")

quiz_game()
