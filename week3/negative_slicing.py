my_str = "picnic"
i = len(my_str)

print("4th to last character (-4:-1) not inclusive of last: ", my_str[-4:-1])
print("")
while i > 0:
    print("characters after the", -i,
          "character from the right including the", -i, "character: ", my_str[-i:])
    i -= 1
i = len(my_str)
while -i < 0:
    print("characters before the", -i+1, "charactes from the right not including the", -
          i+1, "character from the right: ", my_str[:-i+1])
    # print(-i+1)
    i -= 1

