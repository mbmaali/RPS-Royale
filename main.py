import random
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

print("welcome to RPS Royale!")
print("the first to get 2 wins in rounds, wins the game ")
print("enter 'r' for rock, 'p' for paper, or 's' for scissors")
print("you can also type 'rock', 'paper', 'scissors' or 'q' to quit anytime")

player_wins = 0
computer_wins = 0
total_wins = 0
total_losses = 0

moves = {"r": "rock", "p": "paper", "s": "scissors"}
win_color = Fore.GREEN
lost_color = Fore.RED

def check_winner(player, computer):
    global player_wins, computer_wins
    if player == computer:
        print("its a tie!")
    elif (player == "r" and computer == "s") or \
         (player == "p" and computer == "r") or \
         (player == "s" and computer == "p"):
        print(f"{win_color}you won this round!")
        player_wins += 1
    else:
        print(f"{lost_color}you lost this round!")
        computer_wins += 1

def get_computer_choice():
    return random.choice(list(moves.keys()))

def get_player_choice():
    while True:
        choice = input("your move: ").lower()
        if choice in ["r","p","s"]:
            return choice
        elif choice in ["rock","paper","scissors"]:
            return choice[0]
        elif choice in ["q","quit"]:
            print("thanks for playing!")
            exit()
        else:
            print("this is not a valid move, please try again using (r, p, s).")

def display_score(round_number):
    print(f"--- Round {round_number} ---")
    print(f"score: player {player_wins} - {computer_wins} computer")
    print("--------------------")

def play_match(best_of):
    global player_wins, computer_wins, total_wins, total_losses
    player_wins = 0
    computer_wins = 0
    round_number = 1
    target_wins = (best_of // 2) + 1

    while player_wins < target_wins and computer_wins < target_wins:
        time.sleep(0.5)
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"the computer move: {computer_choice}")
        time.sleep(0.5)
        check_winner(player_choice, computer_choice)
        display_score(round_number)
        round_number += 1
        time.sleep(0.5)

    print("====================")
    if player_wins == target_wins:
        print(f"{win_color}YOU WON!!!!!!")
        total_wins += 1
    else:
        print(f"{lost_color}YOU LOST! BETTER LUCK NEXT TIME....")
        total_losses += 1
    print(f"TOTAL WINS: {total_wins} | TOTAL LOSSES: {total_losses}")

def main():
    while True:
        try:
            best_of = int(input("choose match length (best of 3,5,7 etc.): "))
            if best_of % 2 == 0 or best_of <= 0:
                print("please choose an odd positive number")
                continue
        except ValueError:
            print("please enter a valid number")
            continue
        play_match(best_of)
        play_again = input("play another match? (y/n): ").lower()
        if play_again == "n":
            print("thank you for playing!")
            break

if __name__ == "__main__":
    main()
