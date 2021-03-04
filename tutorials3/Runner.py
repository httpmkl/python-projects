# Python file open(fileName, access mode)
# 'r' = read only mode
# 'w' = write only mode (replaces the entire content of a file)
# 'a' = append mode (write without replacing data)


# Python file functions
# read() - returns the whole file
# readline() = returns one line of the file
# readlines() = returns ALL lines in a list (1 line per entry)

# write() = write the listed string to the file


class Writer:

    def writeOverFile(self, fileName, stringData):
        try:
            with open(fileName, 'w') as writer:
                # Use file.[insert function]() functionality here
                writer.write(stringData)
        except IOError:
            print('Error writing to file: ', fileName)

    def writeToFile(self, fileName, stringData):
        try:
            with open(fileName, 'a') as writer:
                # Use file.[insert function]() functionality here
                writer.write(stringData)
        except IOError:
            print('Error writing to file: ', fileName)


writer = Writer()

writer.writeOverFile('TestFile.txt', 'Here is my first text!\n')
writer.writeToFile('TestFile.txt', 'Here is more text to add to it!\n')


class Reader:

    def readAllDataFromFile(self, fileName):
        try:
            with open(fileName, 'r') as reader:
                data = reader.read()
                return data
        except IOError:
            print('Unable to read from file: ', fileName)

    def readOneLineFromFile(self, fileName):
        try:
            with open(fileName, 'r') as reader:
                data = reader.readline()
                print(data)
        except IOError:
            print('Unable to read from file: ', fileName)

    def removeNewLinesFromData(self, data):
        for i in range(len(data)):  # To loop through data
            data[i] = data[i].replace('\n', '')  # Remove references to new lines
            if len(data[i]) == 0:  # Empty entries in data
                data.remove(data[i])
                i -= 1  # Move back a step (since the list is now 1 shorter)
        return data


# Processing string data basics
# Delimiter - the characters that separate our strings into individual sections
# Tokens - the individual strings that are separated by delimiters

# Hello, friend. I want to go to the store


reader = Reader()
data = reader.readAllDataFromFile('TestFile.txt')
print(data)


# Puts every word in a list
allWords = data.split()  # Empty space delimiter
print(allWords)


# Puts every sentence in a list
subWordList = data.split('!')  # Exclamation point delimiter
print(subWordList)

finalData = reader.removeNewLinesFromData(subWordList)
print(finalData)

fileContents = list()

try:
    with open('TestFile.txt', 'r') as reader:
        fileContents.append(reader.readline())
        fileContents.append(reader.readline())
except IOError:
    print('Error reading!')

print(fileContents)

