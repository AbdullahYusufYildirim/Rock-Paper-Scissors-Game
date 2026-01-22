
from random import choice

while True:
    user_choice = input("Enter a choice(Rock,Paper,Scissor): )")
    possible_choices = ['Rock', 'Paper', 'Scissor']
    computer_choice = choice(possible_choices)
    print(f"You chose {user_choice} computer chose {computer_choice}")
    if user_choice == computer_choice :
        print(f"Both players choce {user_choice} İt's a draw ")
    elif user_choice == "Rock" :
        if computer_choice == "Paper" :
            print("Paper covers rock so computer win and  you are lose ")
        elif computer_choice == "Scissor" :
            print("Rock broke Scissor so  computer lose and you are win ")




