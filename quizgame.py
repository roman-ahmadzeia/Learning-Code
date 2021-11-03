print ("Computer Science Quiz!")
print("_________________________")
questions = {
    "When was Python Created? " : "A",
    "Who invented the company Apple?:" : "C",
    "How many bytes do a single character take? ": "B",
    "Is Computer Science amazing? " : "B"}
answers = [
    ["A: 1991", "B. 2010","C. 2003", "D. 2020"],
    ["A: Spongebob", "B. Justin Trudeau", "C. Steve Jobs", "D. Tim Cook"],
    ["A. 5", "B. 4", "C. 16", "D. 1"],
    ["A. No", "B. Yes"]]

def new_game():
    question_num = 1
    guesses = []
    correct_guesses = 0

    for key in questions:
        print(key)
        for i in answers[question_num-1]:
            print(i)
        guess = input(" ANSWER: ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses,guesses)
    play_again()

def check_answer(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1

    else:
        print("Wrong")
        return 0

def display_score(correct_guesses, guesses):
    print("\n Correct Guesses: ",end='')
    for i in questions:
        print (questions.get(i), end='')
    print("\n Your guesses: ", end='')
    for i in guesses:
        print (i, end='')
    print (f'\n Score: {correct_guesses}/4')

def play_again():
    x = input("To play again press F: ")
    if x == "F":
        new_game()

new_game()

