import random

player_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    player_input = input("Rock, Paper, Scissor and Q to quit: ").lower()
    if player_input == "q":
        break

    if player_input not in options:
        print("Invalid input")
        break
        
    computer_pick = random.choice(options)
    print("Computer picked", computer_pick + ".")
    
    if player_input == computer_pick:
        print("It's a tie")
        
    elif player_input == "rock" and computer_pick == "scissors":
        print("You won!")
        player_wins += 1

    elif player_input == "paper" and computer_pick == "rock":
        print("You won!")
        player_wins += 1

    elif player_input == "scissors" and computer_pick == "paper":
        print("You won!")
        player_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", player_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")