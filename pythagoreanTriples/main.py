"""

Program which finds Pythagorean triples

Made by Nora Calif, 2022

Definitions:
    - Primitive/non-multiple triples; Triples with a & b coprime
        Ex. Accepting multiples allows for 6, 8, 10, derived from the primitive triple 3, 4, 5
            Preventing multiples creates a graph with defined lines amidst the scattered points
    - Repeat triples; Triples with a & b rearranged
        Ex. Accepting repeats allows for 4, 3, 5, which is 3, 4, 5 rearranged
            Preventing repeats creates a graph with points north of y = x

"""

import math
from math import gcd
import matplotlib.pyplot as plot

def py_triples(values, repeats, multiples):
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
                if c.is_integer(): # Checks for whether c is an integer (aka, pythagorean triple)
                    if repeats and multiples: # Includes non-primitive & repeated triples
                        triples.append([a, b, int(c)])
                    elif repeats: # Includes repeats, but just primitive triples
                        if gcd(a, b) == 1: # Only appends primitive triples
                            triples.append([a, b, int(c)])
                    elif multiples: # Includes non-primitive triples, but no repeats
                        if a < b: # Avoids repeats
                            triples.append([a, b, int(c)])
                    else: # Excludes non-primitive and repeated triples
                        if gcd(a, b) == 1: # Only appends primitive triples
                            if a < b: # Avoids repeats
                                triples.append([a, b, int(c)])
        notDone = False

    return triples # Returns the list of pythagorean triples

def num_of_triples(values, repeats, multiples):
    "Prints the number of pythagorean triples in a given range"

    print(len(py_triples(values, repeats, multiples))) # Prints length of triples at given range
    # Decent speed for a range of numbers <1000

def superscript(n):
    "Provides superscript text for the equations"

    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])

def print_triples(values, repeats, multiples):
    "Prints the equations for Pythagorean triples in a given range"
    triples = py_triples(values, repeats, multiples)

    for i in range(0, len(triples)):
        triple = triples[i] # Separates each Pythagorean triple into it's own list
        print(str(triple[0]) + superscript(2) + " + " + str(triple[1]) + superscript(2) + " = " + str(triple[2]) + superscript(2))
        # Prints the equation for each Pythagorean triple

def graph_triples(values, repeats, multiples):
    "Graphs the Pythagorean triples in a given range"

    triples = py_triples(values, repeats, multiples) # Gathers the list of triples
    x = [] # Creates a list of x values
    y = [] # Creates a list of y values

    for i in range(0, len(triples)):
        triple = triples[i] # Accesses individual Pythagorean triple
        # Adds a to list of x values, and b to y values
        x.append(triple[0])
        y.append(triple[1])

    # Graphs and displays scatter plot
    plot.scatter(x, y, s=3)
    plot.show()


graph_triples(2000, True, True)