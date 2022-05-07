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


print("Using Lambda")
# Use of lambdas:
print("The sum of numbers: ", reduce(lambda x, y: x + y, numbers))
print("The sum of numbers: ", reduce(lambda x, y: x + y, numbers))
print("Even numbers from numbers:", [num for num in filter(lambda x: x % 2 == 0, numbers)])
print("Square of numbers:", [num for num in map(lambda x: x ** 2, numbers)])
