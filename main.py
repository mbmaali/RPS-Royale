import random
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

print("welcome to RPS Royale!")
print("the first to get 2 wins in rounds, wins the game ")
print("enter 'r' for rock, 'p' for paper, or 's' for scissors")
print("you can also type 'rock', 'paper', 'scissors' or 'q' to quit anytime")

player2_wins = 0
player_wins = 0
computer_wins = 0
total_wins = 0
total_losses = 0

moves = {"r": "rock", "p": "paper", "s": "scissors"}
win_color = Fore.GREEN
lost_color = Fore.RED

def check_winner_mode1(player, computer):
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

def check_winner_mode2(player1, player2):
    global player_wins, player2_wins
    if player1 == player2:
        print("its a tie!")
    elif (player1 == "r" and player2 == "s") or \
         (player1 == "p" and player2 == "r") or \
         (player1 == "s" and player2 == "p"):
        print(f"{win_color}Player 1 won this round!")
        player_wins += 1
    else:
        print(f"{lost_color}Player 2 won this round!")
        player2_wins += 1

def get_computer_choice():
    return random.choice(list(moves.keys()))

def get_player_choice(player_name="Player"):
    while True:
        choice = input(f"{player_name} move: ").lower()
        if choice in ["r","p","s"]:
            return choice
        elif choice in ["rock","paper","scissors"]:
            return choice[0]
        elif choice in ["q","quit"]:
            print("thanks for playing!")
            exit()
        else:
            print("this is not a valid move, please try again using (r, p, s).")

def display_score(round_number, mode):
    print(f"--- Round {round_number} ---")
    if mode == 1:
        print(f"score: player {player_wins} - {computer_wins} computer")
    else:
        print(f"score: Player 1 {player_wins} - {player2_wins} Player 2")
    print("--------------------")

def play_match(best_of, mode):
    global player_wins, computer_wins, total_wins, total_losses, player2_wins

    player_wins = 0
    computer_wins = 0
    player2_wins = 0
    round_number = 1
    target_wins = (best_of // 2) + 1

    if mode == 1:     
        while player_wins < target_wins and computer_wins < target_wins:
            player_choice = get_player_choice()
            computer_choice = get_computer_choice()
            print(f"the computer move: {computer_choice}")
            time.sleep(0.5)
            check_winner_mode1(player_choice, computer_choice)
            display_score(round_number, mode)
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

    elif mode == 2:
        while player_wins < target_wins and player2_wins < target_wins:
            player1_choice = get_player_choice("Player 1")
            player2_choice = get_player_choice("Player 2")
            time.sleep(0.5)
            check_winner_mode2(player1_choice, player2_choice)
            display_score(round_number, mode)
            round_number += 1
        
        if player_wins == target_wins:
            print(f"{win_color}PLAYER 1 WON THE MATCH!!!!!!")
        else:
            print(f"{win_color}PLAYER 2 WON THE MATCH!!!!!!")

def main():
    while True:
        print("Modes available in the game:")
        print("1. play againdst the computer")
        print("2. play against another player on the device")
        mode = int(input("choose mode: ")) 
        if mode != 1 and mode != 2:
            print("please enter 1 or 2")
            continue

        try:
            best_of = int(input("choose match length (best of 3,5,7 etc.): "))
            if best_of % 2 == 0 or best_of <= 0:
                print("please choose an odd positive number")
                continue
        except ValueError:
            print("please enter a valid number")
            continue

        play_match(best_of, mode)
        play_again = input("play another match? (y/n): ").lower()
        if play_again == "n":
            print("thank you for playing!")
            break

if __name__ == "__main__":
    main()
