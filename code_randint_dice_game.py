from random import randint
import time


class COLOR:
    BLUE = '\033[34m'
    RED = '\033[31m'
    BLACK = '\033[30m'


print(f"Hi!\n\
This is a dice game for two. Enter your name and you will get 5 dices.\n\
The computer will throw them for you and print your points.\n\
Each player will start with score of 101, this one who first reaching 0 will win the game.\n\
(Your points will be added if your score is negative!)\n")

player_one_name = input(f"{COLOR.BLACK}Enter your name, player one: ")
print(f"{COLOR.BLUE}{player_one_name}, you got 5 dices and your score is 101.\n")
time.sleep(1)
player_two_name = input(f"{COLOR.BLACK}Enter your name, player two: ")
print(f"{COLOR.RED}{player_two_name}, you got 5 dices and your score is 101.")
print()
time.sleep(1)

count_dice = 5
side_dice = 6

player_one_score = 101
player_two_score = 101
points_from_five_trow = 0
points_list = []


def five_trow():
    global count_dice, side_dice, points_from_five_trow, points_list

    for _ in range(count_dice):
        points = randint(1, side_dice)
        points_list += [points]
        points_from_five_trow += points


while True:
    if player_one_score == 0:
        print(f"{COLOR.BLUE}Congratulations, {player_one_name.upper()}!!!")
        break

    elif player_two_score == 0:
        print(f"{COLOR.RED}Congratulations, {player_two_name.upper()}!!!")
        break

    # for player one
    five_trow()
    print(f"{COLOR.BLUE}{player_one_name}, your points from the five dices are: {points_from_five_trow} {points_list}")
    if player_one_score > 0:
        player_one_score -= points_from_five_trow
    elif player_one_score < 0:
        player_one_score += points_from_five_trow

    print(f"{COLOR.BLUE}{player_one_name}, your score is: {player_one_score}")
    points_from_five_trow = 0
    points_list = []
    print()

    # for player two
    five_trow()
    print(f"{COLOR.RED}{player_two_name}, your points from the five dices are: {points_from_five_trow} {points_list}")
    if player_two_score > 0:
        player_two_score -= points_from_five_trow
    elif player_one_score < 0:
        player_two_score += points_from_five_trow

    print(f"{COLOR.RED}{player_two_name}, your score is: {player_two_score}")
    points_from_five_trow = 0
    points_list = []
    print()

print()
print(f"{COLOR.BLACK}But that is not all!\n\
Тo get your reward, you must guess a number from {COLOR.BLUE}1 {COLOR.BLACK}to {COLOR.RED}10!")

computer_number = randint(1, 10)
while True:
    player_number = input(f"{COLOR.BLACK}Enter a number: ")
    if not player_number.isdigit():
        print("Invalid input!")
    else:
        player_number = int(player_number)
        if player_number < computer_number:
            print(f"{COLOR.RED}Try with bigger number!")
        elif player_number > computer_number:
            print(f"{COLOR.BLUE}Try with lower number!")
        else:
            print(f"{COLOR.BLACK}\nYou guess it!!!\n")
            break

print("Your reward is that incredible experience.\n\
You welcome!")
