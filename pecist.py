import random

rock = "rock!!!"
paper = "paper!!!"
scissors = "scissors!!!"
game = [rock,paper,scissors]

user_turn = int(input("choose 0 for rock,1 for paper or 2 for scissors: "))

if user_turn >= 3 or user_turn < 0:
    print("Not acceptable number!!! ")
    quit()
print(f"  Your   choose:{game[user_turn]}")

cput_turn = random.randint(0,2)
print(f"computer choose:{game[cput_turn]} ")

if user_turn == 0  and cput_turn ==2 :
    print("You win!!! ")
elif cput_turn == 0 and user_turn ==2:
    print("You lose!!! ")
elif cput_turn > user_turn:
    print("You lose!!! ")
elif user_turn > cput_turn:
    print("You win!!! ")
elif cput_turn == user_turn:
    print("Draw!!! ")
