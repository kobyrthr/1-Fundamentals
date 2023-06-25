import random

high_score = 0


def dice_game():
    print("Current High Score is: " + str(high_score))
    print("1) Roll Dice")
    print("2) Leave Game")
    player_choice = input("Enter your choice: ")
    if player_choice == "1":
        die_1 = random.randint(0,6)
        die_2 = random.randint(0,6)
        print(die_1,die_2)
        dice_game()
    elif player_choice == "2":
        print("Goodbye!")
        quit()


dice_game()
