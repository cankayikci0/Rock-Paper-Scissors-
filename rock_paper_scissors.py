import random
import time
actions = ["Rock", "Paper", "Scissors"]
game_continue = True
counter = 3;
print("Welcome to the 'Rock-Paper-Scissors' Game")
while counter > 0:
    print(counter)
    counter -= 1
    time.sleep(1)
print("Game Started")
while game_continue:
    player1 = random.choice(actions)
    player2 = random.choice(actions)
    print("Player1 selected: " + player1 + "  Player2 selected: " + player2)
    if player1 == player2:
        print("It's a tie!")
    elif player1 == "Rock":
        if player2 == "Paper":
            print("Player2 wins!")
        elif player2 == "Scissors":
            print("Player1 wins!")
    elif player1 == "Paper":
        if player2 == "Scissors":
            print("Player2 wins!")
        elif player2 == "Rock":
            print("Player1 wins!")
    else:
        if player2 == "Rock":
            print("Player2 wins!")
        elif player2 == "Paper":
            print("Player1 wins!")
    selected = input('Do you want to continue? (Yes/No):')
    if selected == "No":
        game_continue = False
    else:
        print("Game continuing")
    print("Game Finished.");
