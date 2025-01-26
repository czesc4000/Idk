import random


numbers = (random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5))
your_anwser = (input("your guess"))


if your_anwser[0] == numbers[0] or numbers[1] or numbers[2] or numbers[3] or numbers[4]:
    print("")
    if your_anwser[0] == numbers[0]:
        print("+")
    elif your_anwser[0] == numbers[1] or numbers[2] or numbers[3] or numbers[4]:
        print("-")
elif your_anwser[0] != numbers[0] or numbers[1] or numbers[2] or numbers[3] or numbers[4]:
    print("X")



 















print(your_anwser)
print(numbers)
