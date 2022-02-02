import random

lowestNum = 1
highestNum = 10
guessedNum = None

randomNumber = random.randint(lowestNum, highestNum)

guessedNum = int(input("Please guess a number between {} and {}".format(lowestNum, highestNum)))

if guessedNum is randomNumber:
  print("Woh!!! You've guessed it right! Looks like someone's having a lucky day 😎")
else:
  if guessedNum < randomNumber:
    print("Please guess it higher")
  else:
    print("Please guess it lower")
  guessedNum = int(input())
  
  if guessedNum is randomNumber:
    print("Yes! You got it right. 😀")
  else:
    print("No! You're out of luck 🙁")
    print("The right answer is {}".format(randomNumber))
    print("Better luch next time 🤓")
