for X in range (6):
    for Y in range (6):
        print("*",end='')
    print("\r")
print(".................")


for X in range (6):
    for Y in range (6):
        print("1",end='')
    print("\r")
print(".................")

for X in range (6):
    for Y in range (6):
        print(X,end='')
    print("\r")
print(".................")

for X in range (6):
    for Y in range (6):
        print(Y,end='')
    print("\r")
print(".................")

for X in range (6):
    for Y in range (X+1):
        print("*",end='')
    print("\r")
print(".................")