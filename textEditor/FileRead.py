# Python file open(fileName, access mode) access modes
# 'r' = read only mode
# 'w' = write only mode - erases everything that was there already!
# 'a' = append mode (write without replacing data)


# Python file functions
# read() - return whole file
# readline() - returns one line of the file
# readlines() = returns ALL lines in a list (1 line per entry)

class FileRead:

    def __init__(self):
        pass

    def readFirstLineFromFile(self, filename):
        ''' Print out the contents from the first line of a file '''
        try:
            with open(filename, 'r') as reader:
                data = reader.readline()
                print(data)
        except IOError:
            print('Unable to read from file: ', filename)

    def readFileLineByLine(self, fileName):
        ''' Prints out contents of the file line by line '''
        with open(fileName, 'r') as reader:
            line = reader.readline()
            while line:  # loop as long as line is defined (stops after last line is read and returns null)
                print(line)
                line = reader.readline()  # update line with next line data

    def getFileAllLines(self, fileName):
        ''' Returns a list of file contents, 1 line per entry '''
        data = list()

        with open(fileName, 'r') as reader:
            line = reader.readline()
            while line:  # loop as long as line is defined (stops after last line is read and returns null)
                data.append(line)  # add line to data
                line = reader.readline()  # update line with next line data
        return data  # return list containing all data after file reading complete

    def getAllDataFromFile(self, fileName):
        ''' Returns a String containing all data from file '''
        try:
            with open(fileName, 'r') as reader:
                data = reader.read()
                return data
        except IOError:
            print('Unable to read from file: ', fileName)

    # Allows us to clean up a list of data to remove '\n' (newline) content from it
    def removeNewlinesFromData(self, data):
        ''' Returns a string with all \n (newline) content removed '''
        for i in range(len(data)):  # loop through all data
            data[i] = data[i].replace("\n", "")  # remove all references to new lines in data
            if len(data[i]) == 0:  # if there are now empty entries in the data, remove them!
                data.remove(data[i])
                i -= 1  # after removing an entry, we need to move back a step (the list is now 1 shorter)
        return data

    def numOfLinesInFile(self, fileName):
        ''' Returns the total number of lines in a file '''
        data = self.getAllDataFromFile(fileName)
        linesInData = data.split('\n')
        print(len(linesInData))  # prints out the amount of tokens separated by '\n' (lines)

    def numOfWordsInFile(self, fileName):
        ''' Returns the total number of words in a file '''
        data = self.getAllDataFromFile(fileName)
        wordsInData = data.split()
        print(len(wordsInData)) # prints out the amount of tokens separated by ' ' (words)

    def numOfCharactersInFile(self, fileName):
        ''' Returns the amount of characters in a file '''
        char = 0
        with open(fileName, 'r') as reader:
            line = reader.readline()
            while line:  # loop as long as line is defined (stops after last line is read and returns null)
                char += len(line)  # updates the char counter with the length of each word
                line = reader.readline()  # update line with next line data
        print(char)

    def checkIfFileHasPhrase(self, fileName, phrase):
        ''' Returns whether or not the file has the given phrase '''
        hasPhrase = False

        rawData = self.getFileAllLines(fileName)
        data = self.removeNewlinesFromData(rawData)

        for line in data:
            if line == phrase:  # if a line matches the given phrase
                hasPhrase = True
                print(f"The file has the word(s) '{phrase}'")
                break  # loop ends

        if not hasPhrase:
            print(f"The file does not have the word(s) '{phrase}'")

    def returnWordsOfLength(self, fileName, length):
        ''' Returns words with the given amount of characters '''
        try:
            length = int(length) + 1
            data = []

            with open(fileName, 'r') as reader:
                line = reader.readline()
                while line:  # loop as long as line is defined (stops after last line is read and returns null)
                    if len(line) == length:
                        data.append(line)  # add line to data
                    line = reader.readline()  # update line with next line data

            if len(data) > 0:
                self.removeNewlinesFromData(data)  # so the output doesnt show any \n
                print(data)
            else:  # no words were added to the data list
                print('No words found with this amount of characters')
        except ValueError:
            print(f"Unable to check for words with '{length}' characters")