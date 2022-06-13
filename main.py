
import random
from tkinter import W

CPU_wins= 0
player_wins= 0


def Choose_Option():
    user_choice= input("GAMETIME!!! Choose Rock, Paper, Scissors: ")
    if user_choice in ("Rock", "rock", "r", "R"):
        user_choice= "r"
    elif user_choice in ("Paper", "paper", "p", "P"):
        user_choice= "p"
    elif user_choice in ("Scissors", "scissors", "s", "S"):
        user_choice= "s"
    else:
        print("Invalid Choice, Try Again")
        Choose_Option()
    return user_choice

def Computer_Option():
    comp_choice = random.randint (1,3)
    if comp_choice ==1:
        comp_choice ="r"
    if comp_choice ==2:
        comp_choice ="p"
    else:
        comp_choice= "s"
        return comp_choice
        
while True:
    print("")
    user_choice= Choose_Option()
    comp_choice= Computer_Option()
    print("")

    if user_choice=="r":
        if comp_choice=="r":
            print("Player(Rock) , CPU(Rock)... It's a TIE!")
        elif comp_choice=="p":
            print("Player(Rock) , CPU(Paper). Paper beats Rock... YOU LOSE!")
            CPU_wins += 1   
        elif comp_choice=="s":
            print("Player(Rock) , CPU(Scissors). Rock beats Scissors... YOU WIN!")
            player_wins += 1  

    elif user_choice=="p":
        if comp_choice=="r":
            print("Player(Paper) , CPU(Rock). Paper beats Rock... YOU WIN!")
            player_wins +=1
        elif comp_choice=="s":
            print("Player(Paper) , CPU(Scissors). Scissors beats Paper... YOU LOSE!")
            CPU_wins += 1
        elif comp_choice=="p":
            print("Player(Paper) , CPU(Paper)... It's a TIE!")

    elif user_choice=="s":
        if comp_choice=="r":
            print("Player(Scissors) , CPU(Rock). Rock beats Scissors... YOU LOSE!")
            CPU_wins +=1
        elif comp_choice=="p":
            print("Player(Scissors) , CPU(Paper). Scissors beats Paper... YOU WIN!")
            player_wins += 1
        elif comp_choice=="s":
            print("Player(Scissors) , CPU(Scissors)... It's a TIE!")

    print("")
    print("Player wins: " + str(player_wins))
    print("CPU wins: " + str(CPU_wins))
    print("")

    user_choice = input("Play Again? (Yes/No)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N" "n", "No", "no"]:
        break
    else:
        break






