print("**************************")
print("Welcome to the game of Rock, Paper and Scissors")
print("**************************")

user_move = input("Enter your move (rock/paper/scissors): ")
print(f"user input is : {user_move}")
user_move = user_move.lower()

valid_moves = ('rock', 'paper', 'scissors')
if user_move not in valid_moves:
    print("Your move was invalid. Please start the game again")
    exit()
print(f"Your move was: {user_move}")

# Importing random module
import random
my_move = random.choice(valid_moves)
print(f"My move is: {my_move}")

# Logic for winning or losing the game
if user_move == 'rock' and my_move == 'paper':
    print("Paper beats rock, I won ! :D")
elif user_move == 'rock' and my_move == 'scissors':
    print("Rock beats scissors, You won ! :(")
elif user_move == 'paper' and my_move == 'scissors':
    print("Scissors beats paper, I won ! :D")
elif user_move == 'paper' and my_move == 'rock':
    print("Paper beats rock, You won ! :(")
elif user_move == 'scissors' and my_move == 'paper':
    print("Scissors beats paper, You won ! :(")
elif user_move == 'scissors' and my_move == 'rock':
    print("Rock beats scissors, I won ! :D")
else:
    print("Seems like a draw. Let's play again!")