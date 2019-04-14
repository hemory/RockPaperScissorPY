import os
import sys
# Variables
player1_count = 0
player2_count = 0
keep_going = True
p1_wins = "PLAYER ONE WINS"
p2_wins = "PLAYER TWO WINS"

weapons = {
    'R': """
      _____
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    'P': """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)    
    """,
    'S': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)    
    """
}


# Methods
def player_score():
    print(f"Player One Score: {player1_count} Player Two Score: {player2_count}")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# The Game
while keep_going:
    user1_choice = input("""
    Player One Select Throw:
    'R': Rock
    'P': Paper
    'S': Scissors
    """).upper()
    cls()
    user2_choice = input("""
    Player Two Select Throw:
    'R': Rock
    'P': Paper
    'S': Scissors
    """).upper()
    cls()

    if user1_choice == user2_choice:
        print("You both had the same choice go again")
        player_score()
    elif user1_choice == 'R' and user2_choice == 'S':
        print(f"""{weapons['R']}
        BEATS
        {weapons['S']}""")
        print(p1_wins)
        player1_count += 1
        player_score()
    elif user1_choice == 'S' and user2_choice == 'P':
        print(f"""{weapons['S']}
                BEATS
                {weapons['P']}""")
        print(p1_wins)
        player1_count += 1
        player_score()
    elif user1_choice == 'P' and user2_choice == 'R':
        print(f"""{weapons['P']}
                BEATS
                {weapons['R']}""")
        print(p1_wins)
        player1_count += 1
        player_score()
    elif user2_choice == 'R' and user1_choice == 'S':
        print(f"""{weapons['R']}
                BEATS
                {weapons['S']}""")
        print(p2_wins)
        player2_count += 1
        player_score()
    elif user2_choice == 'S' and user1_choice == 'P':
        print(f"""{weapons['S']}
                BEATS
                {weapons['P']}""")
        print(p2_wins)
        player2_count += 1
        player_score()
    elif user2_choice == 'P' and user1_choice == 'R':
        print("Paper beats Rock, Player two wins!")
        print(f"""{weapons['P']}
                BEATS
                {weapons['R']}""")
        print(p2_wins)
        player2_count += 1
        player_score()
    elif user1_choice or user2_choice != 'R' or 'P' or 'S':
        print("Players must choose a valid weapon")
    option = input("Continue? Y/N ")
    if option.upper() == 'N':
        keep_going = False

print("\nThanks for playing")
sys.exit()
