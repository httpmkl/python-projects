class SavedGame:

    def __init__(self):
        pass

    def writeStringOverFile(self, stringData):
        ''' Write String data to file, overwriting previous file contents '''
        try:
            with open('savepoints.txt', 'w') as writer:
                writer.write(stringData)
        except IOError:
            print('Error writing to file: ', 'savepoints.txt')

    def getFileAllLines(self):
        ''' Returns a list of file contents, 1 line per entry '''
        data = list()

        with open('savepoints.txt', 'r') as reader:
            line = reader.readline()
            while line:  # loop as long as line is defined (stops after last line is read and returns null)
                data.append(line)  # add line to data
                line = reader.readline()  # update line with next line data

        cleanData = self.removeNewlinesFromData(self, data) # cleans data of \n
        return cleanData  # return list containing all data after file reading complete

    def removeNewlinesFromData(self, data):
        ''' Returns a file with all \n (newline) content removed '''
        for i in range(len(data)):  # loop through all data
            data[i] = data[i].replace("\n", "")  # remove all references to new lines in data
            if len(data[i]) == 0:  # if there are now empty entries in the data, remove them!
                data.remove(data[i])
                i -= 1  # after removing an entry, we need to move back a step (the list is now 1 shorter)

        return data