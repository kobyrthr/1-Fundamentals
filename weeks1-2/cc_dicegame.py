import random

high_score = 0


def dice_game():
    global high_score
    print("Current High Score is: " + str(high_score))
    print("1) Roll Dice")
    print("2) Leave Game")
    player_choice = input("Enter your choice: ")
    if player_choice == "1":
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        dice_sum = die_2+die_1
        print("you rolled a..." + str(die_1) + "\n" + "you rolled a..." + str(die_2) + "\n" + "you have rolled a total of " + str(dice_sum))
        if dice_sum > high_score:
            print("New highscore!")
            high_score = dice_sum
        dice_game()
    elif player_choice == "2":
        print("Goodbye!")
        quit()


dice_game()
