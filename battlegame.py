
def game():
    wizard ="Wizard"
    elf = "Elf"
    human = "Human"
    orc = "Orc"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 80

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 30

    dragon_hp = 300
    dragon_damage = 50
    while True:
        print("1) "+wizard)
        print("2) "+elf)
        print("3) "+human)
        print("4) "+orc)
        print("5) exit")
        character = input("Choose your character: ")
        if character == "1" or character.lower() == "wizard":
            character = wizard
            my_hp=wizard_hp
            my_damage=wizard_damage
            break
        elif character == "2" or character.lower() == "elf":
            character = elf
            my_hp=elf_hp
            my_damage=elf_damage
            break
        elif character == "3" or character.lower() == "human":
            character = human
            my_hp=human_hp
            my_damage=human_damage
            break
        elif character == "4" or character.lower() == "orc":
            character = orc
            my_hp=orc_hp
            my_damage=orc_damage
            break
        elif character.lower() == "exit":
            quit()
        else: 
            print("Unknown character")

        print("Your character is: "+character +". "+ character + " has hp of "+ str(my_hp) + " and damage of "+str(my_damage)+".")

    #BATTLE WITH THE DRAGON!

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hp is: "+str(dragon_hp))
        if dragon_hp <= 0:
            print("The Dragon has lost the battle.")
            break
        my_hp = my_hp - dragon_damage
        print("The Dragon attacked the "+ character)
        print("The "+ character + "'s hp is: "+str(my_hp))
        if my_hp <= 0:
            print("The "+character+" has lost the battle.")
            break

while True:
    game()
    restart = input("Would you like to play again?: (Y/N)")
    if restart == "n" or "N":
        break
    if restart == 'y' or "Y":
        continue
   