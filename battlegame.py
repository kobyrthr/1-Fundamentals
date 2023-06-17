#VARIABLES

wizard ="Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

#CHOOSE YOUR CHARACTER
while True:
    print("1) "+wizard)
    print("2) "+elf)
    print("3) "+human)
    character = input("Choose your character: ")
    if character == "1":
        character = wizard
        my_hp=wizard_hp
        my_damage=wizard_damage
        break
    if character == "2":
        character = elf
        my_hp=elf_hp
        my_damage=elf_damage
        break
    if character == "3":
        character = human
        my_hp=human_hp
        my_damage=human_damage
        break
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