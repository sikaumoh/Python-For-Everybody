friends = ['joseph', 'glenn', 'sally']
# print(friends[1])   # prints out glenn

# lists are mutable (change be edited)
friends[0] = 'Henry'
# print(friends)   # it prints ['Henry', 'glenn', 'sally']

# Using range function
# print(range(4))   # prints 0, 1, 2, 3

# counted loop
for i in range(len(friends)):
    friend = friends[i]
    # print(i, friend)

# Concatenting lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# print(c)

# print(dir(a))  # this is to find the functions to use on lists

# Building lists from scratch
stuff = list()   # OR stuff = []
stuff.append('book')
stuff.append(99)
print(stuff)  # prints ['book', 99]

# in operator
some = [1, 9, 35, 23]
print(9 in some)  # prints TRUE

# You can use list.sort() to arrange items in a list alphabetically

# Split
abc = 'With three words'
stuff = abc.split()   # converts abc into stuff list
# print(stuff)

# split just separates words from delimiter (whitespace or any delimiter)
# you can specify the particular delimiter you want

# Double Split Pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
# print(email)  # prints out stephen.marquard@uct.ac.za
# print(pieces)  # prints out ['stephen.marquard', 'uct.ac.za']

# list comprehension
c = {'a': 10, 'b': 1, 'c': 22}  # a dictionary
print(sorted([(v, k) for k, v in c.items()]))

# Exercises
# Read files and give out a result
# 1
filename = input('Enter file name: ')
filehandle = open(filename)
filelist = filehandle.read().split()
filelist = set(filelist)
list = sorted(list(filelist))
# print(list)

# 2
# Sort words of each line alphabetically
filename = input('Enter file name: ')
filehandle = open(filename)
list = []
for line in filehandle:
    line = line.rstrip()  # Remove space on the right
    line = line.split()  # turn each line into a list
    for word in line:
        if word in list: continue
        list.append(word)
# print(sorted(list))

# 3
# Count number of lines starting with 'From:'
filename = input('Enter file name: ')
filehandle = open(filename)
count = 0
for line in filehandle:
    if not line.startswith('From:'): continue
    line = line.rstrip().split()
    count += 1
    print(line[1])
# print('There were', count, 'lines in the file with From as the first word')

# 4
# Example of each line 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# Get the time that's most frequent
filename = input('Enter file name: ')
filehandler = open(filename)
counts = dict()
for line in filehandler:
    if not line.startswith('From'): continue
    line = line.rstrip().split()
    if len(line) < 3: continue  # guardian against error
    time = line[5].split(':')  # prints out [09, 14, 16]
    hours = time[0]
    counts[hours] = counts.get(hours, 0) + 1
for k, v in sorted([(k, v) for k, v in counts.items()]):
    # print(k, v)
