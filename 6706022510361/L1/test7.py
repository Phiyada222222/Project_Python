import random
print("*** Welcome to the Number Guessing Game!***")
print("I'm thinking of a number between 1 and 100. Can you guss it? ")
f = 1 
M = random.randint(1,100)
print(M)
while True :
    guess = int(input("Enter your Guess :"))
    if guess == M :
        print(f"congratulations!{f}")
        break
    elif guess > M :
        print("Too high")
        f+=1 
    elif guess < M :
        print("Too low!")
        f+=1 

    