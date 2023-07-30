import random
import time
import os
from colorama import Fore

def main():
    casino_balance = 5000000
    user_balance = 1000

    # Display the rules and how to play
    print(Fore.LIGHTMAGENTA_EX + "Welcome To The Casino")
    rules = """
    Rules:
    1. The bet amount must be multiples of 50 $.
    2. The multiplier must be between 1 and 10.
    3. In case of a loss, you will owe the casino the bet amount multiplied by the multiplier.
    4. If the casino balance reaches 0 $, the player wins.
    5. If the player balance reaches 0 $, the casino wins.
    6. Good luck! And remember, "The Casino always wins."
    """

    how_to_play = """
    How to Play:
    1. Enter the bet amount.
    2. Enter the multiplier.
    3. Wait for the result and learn about the win/loss.
    4. If the game continues, enter a new bet.
    """

    print(Fore.YELLOW + rules)
    print(Fore.YELLOW + how_to_play)

    accept = input("Do you accept the rules? (y/n): ")
    if accept != "y":
        print(Fore.YELLOW + "Exited the game without accepting the rules. You must accept the rules to play.")
        return

    def win(bet_amount, multiplier):
        nonlocal casino_balance, user_balance
        winnings = bet_amount * multiplier
        casino_balance -= winnings
        user_balance += winnings
        return winnings

    def lose(bet_amount, multiplier):
        nonlocal casino_balance, user_balance
        loss = bet_amount * multiplier
        casino_balance += bet_amount
        user_balance -= loss
        return loss

    def play():
        nonlocal casino_balance, user_balance
        os.system('cls' if os.name == 'nt' else 'clear')

        print(Fore.YELLOW + f"Your current balance: {user_balance} $")
        bet_amount = int(input("Enter the bet amount (multiples of 50 $): "))

        if bet_amount % 50 != 0 or bet_amount <= 0:
            print(Fore.YELLOW + "Invalid bet amount. Please enter multiples of 50 $.")
            time.sleep(3)
            return

        if bet_amount > user_balance:
            print(Fore.YELLOW + "Insufficient balance. Enter a lower bet amount.")
            time.sleep(3)
            return

        multiplier = int(input("Enter the multiplier (between 1 and 10): "))

        if multiplier < 1 or multiplier > 10:
            print(Fore.YELLOW + "Invalid multiplier. Please enter a value between 1 and 10.")
            time.sleep(3)
            return

        print(Fore.YELLOW + f"Bet amount: {bet_amount} $")
        print(Fore.YELLOW + f"Estimated winnings: {bet_amount * multiplier} $")

        for i in range(3, 0, -1):
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
            print(Fore.YELLOW + f"Your current balance: {user_balance} $")
            print(Fore.YELLOW + f"Bet amount: {bet_amount} $")
            print(Fore.YELLOW + f"Estimated winnings: {bet_amount * multiplier} $")
            print(Fore.YELLOW + f"Remaining time: {i} seconds")
            time.sleep(1)

        if random.random() < 0.5:
            winnings = win(bet_amount, multiplier)
            print(Fore.GREEN + f"Congratulations, you won! Your winnings: {winnings} $")
            time.sleep(3)
        else:
            loss = lose(bet_amount, multiplier)
            print(Fore.RED + f"Sorry, you lost! Your loss: {loss} $")
            time.sleep(3)

        if casino_balance <= 0:
            print(Fore.RED + "Casino Authorities Alerted! Run for Your Life")
            time.sleep(3)

    # Game loop
    while casino_balance > 0 and user_balance > 0:
        play()

    print(Fore.YELLOW + "Game Over.")

if __name__ == "__main__":
    main()