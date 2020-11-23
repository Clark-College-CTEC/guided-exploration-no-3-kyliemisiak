# Guided Exploration No. 3
# Kylie Misiak

# importants the random library
import random

# creates an empty list called 'possible_names'
possible_names = []

# opens a file and stores data in variable 'outputFile'
outputFile = open('rap-names-output.txt', 'w')

# opens the 'rap-names.txt' file, assigns it to dataFile
with open('rap-names.txt', 'r') as dataFile:
    # creates a for loop to iterate through the file
    for name in dataFile:
        # appends the names from the file to the 'possible_names' list, while taking off blank lines
        possible_names.append(name.rstrip())

# asks user for how many rap names they would like
count = int(input('How many rap names would you like to create? '))
# asks user for how long they want the rap name
parts = int(input('How many parts should the name contain? '))

# counted loop for how many rap names the user wants
for i in range(count):
    # creates new blank list, 'name_parts'
    name_parts = []
    # counted loop for length of rap name
    for j in range(parts):
        # gets a random rap name/s and appends to 'name_parts' list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

    # joins the 'name_parts' list with the 'outputFile' variable
    outputFile.write(f"{' '.join(name_parts)}\n")
    # prints the rap names
    print(f"{' '.join(name_parts)}")

    # closes the file at the end of program
outputFile.close()
