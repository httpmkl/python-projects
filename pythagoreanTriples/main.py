import math
from math import gcd

def py_triples(values):
    "Finds all Pythagorean triples under a given range"
    nums = list(range(1, int(values) + 1))
    notDone = True
    triples = []

    while notDone: # Creates a while loop
        for i in range(0, int(values)):
            a = int(nums[i])
            for i in range(0, int(values)): # Compares every b value against each a value
                b = int(nums[i])
                c = math.sqrt(math.pow(a,2) + math.pow(b,2)) # Sqrt of a^2 + b^2
                if c.is_integer(): # If c ends in .0 (pythagorean triple)
                    if a < b: # To avoid repeats, for ex. 3,4,5 & 4,3,5
                        if gcd(a, b) == 1: # To search for primitive triples
                            triples.append([a, b, int(c)]) # Adds combo to list of triples
        break

    return triples # Returns the list of pythagorean triples


def num_of_triples(values):
    "Prints the number of pythagorean triples in a given range"

    print(len(py_triples(int(values)))) # Prints length of triples at given range
    # Decent speed for a range of numbers <1000


def superscript(n):
    "Provides superscript text"

    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])


def print_triples(values):
    "Prints the equations for Pythagorean triples under a given range"
    triples = py_triples(int(values))

    for i in range(0, len(triples)):
        triple = triples[i]
        print(str(triple[0]) + superscript(2) + " + " + str(triple[1]) + superscript(2) + " = " + str(triple[2]) + superscript(2))