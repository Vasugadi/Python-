# guess the number
# generates random number-->target
# we have to guess the number
#if guessed  succesfull
#if guessed less than target -- user have to guess greater
#if guessed greater than target -- user have to guess lesser

# we are using random module in python for generating random number
import random
target=random.randint(1,100)#this function will generate random number between 1 and 100
print(target)
while True:
    guess=int(input("guess the number:"))
    if guess==target:
        print("you guessed it right")
        break
    elif guess<target:
        print("guess a greater number")
    else:
        print("guess a lesser number")
print("-----GAME OVER-----")