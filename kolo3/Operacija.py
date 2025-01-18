x = int(input())
y = int(input())
z = int(input())

if x*y == z:
    if x+y == z:
        print(":(")
    else:
        print("*")

elif x+y == z:
    print("+")
else:
    print("sjedi jedan")
