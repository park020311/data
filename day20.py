import random
r = random.randint(1,100)
chance = 7

while chance!=0:
    n = int(input("Input guess number : "))
    if n==r:
        print("correct")
        break

    elif n>r:
        chance = chance - 1
        print(f"{n} > random number (chance : {chance})")

    else:
        chance = chance - 1
        print(f"{n} < random number(chance : {chance})")

print("end.")