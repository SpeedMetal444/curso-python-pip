import random
import sys


def choose_options():
    options = ("piedra", "papel", "tijera")
    user_option = input("Piedra, papel o tijera? ")
    user_option = user_option.lower()
    if user_option not in options:
        print("\n", user_option.upper(), "no es una opción válida amigo\n")
        # continue
        return None, None
    computer_option = random.choice(options)
    print("\nElegiste:", user_option.capitalize())
    print("La computadora eligió:", computer_option.capitalize(), "\n")
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Empate \n")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra gana a tijera\n")
            print("Ganaste\n")
            user_wins += 1
        else:
            print("Papel gana a piedra\n")
            print("La compu te ganó\n")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Papel gana a piedra\n")
            print("Ganaste\n")
            user_wins += 1
        else:
            print("Tijera gana a papel\n")
            print("La compu te ganó\n")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera gana a papel\n")
            print("Ganaste\n")
            user_wins += 1
        else:
            print("Piedra gana a tijera\n")
            print("La compu te ganó\n")
            computer_wins += 1
    return user_wins, computer_wins


def check_winner(user_wins, computer_wins):
    if user_wins == 2:
        print("*" * 19)
        print("|Ganaste el juego!|")
        print("*" * 19, "\n")
        sys.exit()
    elif computer_wins == 2:
        print("*" * 25)
        print("|La compu ganó el juego!|")
        print("*" * 25, "\n")
        sys.exit()


def run_game():
    user_wins = 0
    computer_wins = 0
    rounds = 1

    while True:
        print("*" * 11)
        print("|", "ROUND", rounds, "|")
        print("*" * 11, "\n")
        print("PC=", computer_wins, "USER=", user_wins, "\n")
        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(
            user_option, computer_option, user_wins, computer_wins
        )
        check_winner(user_wins, computer_wins)


run_game()
