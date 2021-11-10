from random import randint

choices = ["PAPER", "ROCK", "SCISSORS"]

def compare(user, computer):
    if user == "ROCK":
        if computer == "ROCK":
            return "TIE"
        if computer == "PAPER":
            return "LOSE"
        if computer == "SCISSORS":
            return "WIN"
    elif user == "PAPER":
        if computer == "ROCK":
            return "WIN"
        if computer == "PAPER":
            return "TIE"
        if computer == "SCISSORS":
            return "LOSE"
    elif user == "SCISSORS":
        if computer == "ROCK":
            return "LOSE"
        if computer == "PAPER":
            return "WIN"
        if computer == "SCISSORS":
            return "TIE"
    else:
        return "ERROR"

while True:
    print("Choose ROCK, PAPER, or SCISSORS:")
    computer = choices[randint(0, 2)]
    user = input()

    print(compare(user, computer))





