# import functools

def addition(x, y):
  return x + y
  
def is_even(x):
  return x % 2 == 0

def get_square(x):
  return x ** 2
  
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("The sum of numbers: ", reduce(addition, numbers))
print("Even numbers from numbers:", [num for num in filter(is_even, numbers)])
print("Square of numbers:", [num for num in map(get_square, numbers)])

# Use of lambdas:
print("\nUsing Lambda")
print("The sum of numbers: ", reduce(lambda x, y: x + y, numbers))
print("Even numbers from numbers:", [num for num in filter(lambda x: x % 2 == 0, numbers)])
print("Square of numbers:", [num for num in map(lambda x: x ** 2, numbers)])


# Use of comprehension and generators
print("\nUsing comprehension and generators")
sum = 0

print("The sum of numbers: ", [num for num in numbers])
print("Even numbers from numbers:", [x for x in numbers if x % 2 == 0])
print("Square of numbers:", [x ** 2 for x in numbers])

print(list(map(lambda x: x ** 2, range(1, 11))))
