import random

target = random.randint(1,50)

while True:
    userChioce= input("Guess the target or Quit:")
    if(userChioce=="Quit"):
        break

    userChioce=int(userChioce)
    if(userChioce==target):
        print("Success:Correct Guess!!")
        break
    elif(userChioce<target):
        print("your number was too small. Take a bigger guess..")
    else:
        print("your number was too big.Take a smaller guess..")

print("-----GAME OVER----")
