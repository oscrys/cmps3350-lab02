# CMPS 3350 - Lab 2
# Prints each command-line argument passed into the program, one per line
from sys import argv

for index in range(1, len(argv)):
    print(f"arg {index}: {argv[index]}")
