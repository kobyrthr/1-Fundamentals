import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_choice = input("Pick a card (or Q to quit): ")
    if user_choice.lower() == "q":
        break
    else:
        drawn_card = random.choice(diamonds)
        hand = hand.append(diamonds.pop(diamonds[drawn_card]))
        print(len(diamonds))