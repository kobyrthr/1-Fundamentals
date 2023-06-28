import random

diamonds = ["AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD"]
hand =[]

while diamonds:
    user_choice = input("Press 'Enter' to pick a card. Press 'Q' then 'Enter' to quit: ")
    if str.lower(user_choice) == "q":
        quit()
    else:
        hand.append(diamonds.pop(random.randrange(len(diamonds))))
        print("Hand: ", hand)
        print("Deck: ", diamonds)
        
if not diamonds:
    print("There are no more cards ot pick.")

