print("String concatination: " + str(123))

print("These " "are " "different " "strings")

diffstrs = "this" " is " "really weired"
print(diffstrs)

print
print


diffnums = "1235"
print(float(diffnums))

print(([1, 2, 3]))

age = 28
retirement = 60

print("I'm currently {0} age old and planning to retire at {2}".format(age, retirement))

print("""
No {0:9} belongs to Max.
No {1:9} belongs to Pierce.
No {2:9} belongs to Alex
No {3:9} belongs to Cassie
""".format(12, 4333, 5949309, 2))

print("""
No {0:>9} belongs to Max.
No {1:>9} belongs to Pierce.
No {2:>9} belongs to Alex
No {3:>9} belongs to Cassie
""".format(12, 4333, 5949309, 2))

print("""
No {0:^9} belongs to Max.
No {1:^9} belongs to Pierce.
No {2:^9} belongs to Alex
No {3:^9} belongs to Cassie
""".format(12, 4333, 5949309, 2))

print("The value of pi is {0} and '{1:20.10f}.'".format(22/7, 22/7))

#print(f"The value of pi is {22/7}")

import platform
print("The current version of python is: {}".format(platform.python_version()))

print("So f-strings are not suppported here, Yet!!!")

print("This is string interpolation which is an old feature of %s %d and not supported after %f" % ('Python', 2, 3.0))
