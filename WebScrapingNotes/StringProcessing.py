# String are immutable (cannot be changed directly)

# 1. Strip whitespace

text = '    this is the message that comes in    '
text = text.strip()  # strips the whitespace
leftIndent = text.rstrip()  # takes whitespace on the right
rightIndent = text.lstrip()  # takes whitespace on the left


# 2. Replace certain content in a string

text = text.replace('the', 'a', 1)  # replaces 'hallo' with 'hello'
# think about how to only replace the last instance of the word, or second, etc.


# 3. Break long strings up into sub-sections (words)
allText = text.split()


# 4. Case management
upper = text.upper()  # all uppercase
lower = text.lower()  # all lowercase
capitalEvery = text.title()  # capitalize every word
capitalFirst = text.capitalize()  # capitalizes first word (in STRING, not necessarily sentence)
inverse = text.swapcase()  # invert the cases


# 5. Reverse contents of a spring
reversedString = ''.join(reversed(text))  # every letter reversed (not entire words)


# 6. Check if certain contents are in a string
if 'mess' in text:  # returns true even if part of a word
    inText = True
else:
    inText = False


# 7. String slicing
text = 'this is the message that comes in'
subText = text[12:16]  # gets elements 12-15 (first num inclusive, second num exclusive)
# [num:] means 'til the end of the string, [:num] means from the start of the string
# this is also good if you want to take out information in the deepest tag layer you want