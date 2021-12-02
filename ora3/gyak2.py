import random
n = random.randint(0, 20)
guess = int(input("Enter an integer from 0 to 20: "))
while n != "guess":
    print
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 0 to 20: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 0 to 20: "))
    else:
        print ("you guessed it!")
        break
    print