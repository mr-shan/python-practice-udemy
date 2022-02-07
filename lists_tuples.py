numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(len("This"))

print(min("thiT"))

print("This is the THE statement".count('t'))
print(numbers.count('c'))

# numbers[0:5] = []
# del numbers[0:1]

# numbers[0::2] = ['a', 'b', 'c', 'd', 'e']
# print(len(numbers[::2]))

# numbers2 = numbers.copy()

# print(id(numbers))
# print(id(numbers2))

for index, item in enumerate(numbers):
  print("At index: {}, value is: {}".format(index, item))
  
print("")

print("s" in "This is string")

new_numbers = [1, 2, 3]

# numbers += new_numbers
# numbers.extend(new_numbers)

floats = [5.3, 2.1, 8.4, 1.6, 9.0, 7.8, 6.2, 3.5, 2.9]

another_floats = floats[-1::-1]
print(floats)
print(another_floats)


first = 0
last = len(another_floats) - 1
while first <= last:
  temp_first = another_floats[first]
  another_floats[first] = another_floats[last]
  another_floats[last] = temp_first
  first += 1
  last -= 1
  
print(another_floats)

del another_floats[:-1]
del another_floats[:-1]

print(another_floats)

food = ["cake", "bread", "pudding", "ice-cream"]
print(food.count("c"))

print(", ".join('This'))

panagram = "the quick brown fox jumps over the lazy dog"

number_string = "1,2,3"
numbers_array = []
for i in number_string.split(','):
  numbers_array.append(int(i))

print(numbers_array)

tple = 1, 2, 3, 4, 5, 6
print(tple)

a, b, c, d, e, f = tple
print(c, d)

print('')

for item in enumerate(food):
  index, food = item #item is an tuple which enumerate returns
  print(index)
