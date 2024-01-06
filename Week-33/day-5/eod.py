from random import choice

leaderboard = [0, 0, 0]  # win/lose/tie


def calculate_leaderboard(condition):  # w ->
    if condition == "w":
        leaderboard[0] += 1
    elif condition == "l":
        leaderboard[1] += 1
    else:
        leaderboard[-1] += 1
    print(
        f"SCORE: You - {leaderboard[0]} | AI - {leaderboard[1]}  | Ties - {leaderboard[-1]}"
    )
    return


# Make a player choice
def make_choice():
    good_inputs = ["rock", "paper", "scissors"]

    choice = input("Rock, Paper, Scissors ? :      ")

    if choice.lower() in good_inputs:
        return choice
    else:
        print("That was not a valid choice. Please try again...")
        return make_choice()


# Make an AI choice


def computer_move():
    ai = choice(["rock", "paper", "scissors"])
    return ai


def check_win(player_move, ai_move):
    # check moves
    win_lose = {
        "rock": ("scissors", "paper"),  # win/lose
        "paper": ("rock", "scissors"),
        "scissors": ("paper", "rock"),
    }

    print(f"You chose: {player_move}, AI chose: {ai_move}")

    if win_lose[f"{player_move}"][0] == ai_move:
        print("YOU WIN")
        calculate_leaderboard("w")
    elif win_lose[f"{player_move}"][1] == ai_move:
        print("Wah wah... you lose.. loserr!")
        calculate_leaderboard("l")
    else:
        print("Its... a tie!")
        calculate_leaderboard("t")

    play_again()


# Func to let me play again
def play_again():
    res = input("Play again? [y/n]     ")
    if res.lower() == "y":
        start_game()
    elif res.lower() == "n":
        return
    else:
        print("You did not pick a valid response")
        return play_again()


def start_game():
    player_move = make_choice()
    ai_move = computer_move()
    check_win(player_move, ai_move)


start_game()
