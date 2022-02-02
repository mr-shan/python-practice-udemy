# for i in range(0,100,5):
#   print(i)

for i in range(-10, 10, 1):
  if i is 0:
    continue
  print(i)
  
foods = ['Milk', 'Tea', 'Bread', 'coffee', 'cake', 'pudding', 'donut']  

# print(len("This is the string"))
# print(len(foods))

item_to_find = 'cake'

for item in foods:
  if item is item_to_find:
    print("Found your " + item_to_find)
    break

print("*"*40)

for i in range(len(foods)):
  print(foods[i])

print("*" * 40)

print("\nGuess my favourite Itlian food")
italian_foods = ["Pizza", "Pasta"]
fav_food = ""
while fav_food not in italian_foods:
  print("Guess my favourite Italian food")
  fav_food = input()
  
print("Yay! You guessed it right!")
  
