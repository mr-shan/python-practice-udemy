name = input("Please enter your name: ")
age = int(input("And how old are you {0}".format(name)))

#print("\nWelcome {0}! {1} years old!!\n".format(name, age))

print("")

if age < 18:
  print("Hey {0}, you're not allowed to drink! :(\nPlease come back after {1} years! :)".format(name, 18-age))

elif age < 22:
  print("Welcome {0}, to the party! :) \nBut remember, NO HARD DRINKS! \nBeer and wine only!!! ;)".format(name))

else:
  print("Welcome {0}, to the party! :) \nHave a great booze!!! ;)".format(name))
