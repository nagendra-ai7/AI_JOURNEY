secret = 7

guess = int(input("guess the number: "))

while guess != secret:
    if guess < secret:
        print("too low!")
    else:
        print("too high!")

    
    guess = int(input("guess again: "))

print("yes you are correct.")


