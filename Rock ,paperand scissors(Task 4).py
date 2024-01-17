import random

options = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
running = True

wins = 0
losses = 0
ties = 0

while running:
    player = None
    computer = random.choice(list(options.keys()))

    while player not in options:
        player = input("Enter a choice (r for rock, p for paper, s for scissors): ").lower()

    print(f"Player: {options[player]}")
    print(f"Computer: {options[computer]}")

    if player == computer:
        print("It's a tie!")
        ties += 1
    elif (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1

    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
