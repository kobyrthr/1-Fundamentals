my_str = "picnic"
i = len(my_str)

# print(my_str[:-2])
# print(my_str[-len(my_str):])

print(my_str[-4:-1])
print("")
while i > 0:
    print("last", i, "characters",my_str[-i:])
    i-=1
i = len(my_str)
while -i < 0:
    print("first", i, "characters",my_str[:-i+1])
    i-=1
# i = len(my_str)
# while i >= 0:
#     print(my_str[:-i+1])
#     i-=1