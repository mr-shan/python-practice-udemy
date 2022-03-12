# import pickle, shelve

# poem = open('./poem.txt', 'r')

# for line in poem:
#     print(line, end='')

# line = poem.readlines()
# print(*line)

# poem.close()

# with open('poem.txt', 'r') as poem:
#     print(poem.read())

# with open('poem.txt', 'r') as poem:
#     line = poem.readline()
#     while line:
#         print(line, end='')
#         line = poem.readline()

# a small program to write tables(padhe) from 1 to 10
# with open('padha.txt', 'w') as file_padha:
#     for table in range(1, 11):
#         print("Table of {}:".format(table), file=file_padha)
#         for index in range(1, 11):
#             file_padha.write(f"{table:2} times {index:2} is {index * table:3}\n")
#         print('*' * 20, file=file_padha)
#         print('\n', file=file_padha)

# Use of pickle library for binary files creation
# evermore = ('Taylor Swift', 'December-2011-2020', 'Pop',
#             (
#                 (1, 'Willow'),
#                 (2, 'Champagne Problem')
#                 )
#             )
#
# with open('evermore.pickle', 'wb') as evermore_file:
#     pickle.dump(evermore, evermore_file)
#     pickle.dump(range(0, 21, 2), evermore_file)
#     pickle.dump(range(1, 20, 2), evermore_file)

# with open('evermore.pickle', 'rb') as evermore_file:
#     evermore = pickle.load(evermore_file)
#     list1 = pickle.load(evermore_file)
#     list2 = pickle.load(evermore_file)
#
# artist, year, genre, tracks = evermore
#
# print(artist)
# print(year)
# print(genre)
# print('Tracks', *tracks)
# print('*' * 20)
# print(list1)
# print(list2)

# with shelve.open('shelve_test') as shelve_test:
#     shelve_test['bmw'] = 'Racing oriented driver focused cars'
#     shelve_test['vw'] = 'Driver oriented mid budget cars'
#     shelve_test['mercedes benz'] = "Comfort oriented luxury cars"
#     shelve_test['volvo'] = 'Ultra safety and ultra luxury'
#

# with shelve.open('shelve_test') as shelve_test:
#     # shelve_test['ferrari'] = 'The italian marvel of super cars'
#     for key, value in shelve_test.items():
#         print(key, ' : ', value)

