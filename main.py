# CMPS 3350 - Lab 2 is all about source control AND git
# Prints each command-line argument passed into the program, one per line
from sys import argv

for index in range(len(argv)-1, 0, -1):
    print(f"arg {index}: {argv[index]}")
