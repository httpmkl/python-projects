from FileEncrypter import FileEncrypter
from FileRead import FileRead
from FileWrite import FileWrite

encrypt = FileEncrypter()
reader = FileRead()
writer = FileWrite()

class FileDecrypter:

    def __init__(self):
        print('File decrypter created!')

    def decodeString(self, string, shift):
        ''' Decrypts the String using the given shift that was previously applied on it '''
        shift *= -1
        decrypt = encrypt.encodeStrAndReturn(string, shift)
        print("\nDecrypted message: " + decrypt)

    def decodeStrAndReturn(self, string, shift):
        ''' Decrypts the String using the given shift that was previously applied on it (and returns the value) '''
        shift *= -1
        decrypt = encrypt.encodeStrAndReturn(string, shift)
        return decrypt

    def decodeData(self, data, shift):
        ''' Decrypts a list of String using the given shift '''
        shift *= -1
        decrypt = encrypt.encodeDataAndReturn(data, shift)
        print('\nDecrypted values:')
        for i in decrypt:
            print(f'-> {i}')

    def decodeFromFile(self, fileName, shift):
        ''' Decrypts the content in a file using the given shift '''
        fileData = reader.getFileAllLines(fileName)

        data = []
        if type(fileData) == str:
            # If a single string is given, it's added to the data list as a single token
            data.append(fileData)
        elif type(fileData) == list:
            # If a list is given, it becomes the data list
            data = fileData

        decryptedData = []

        try:
            if len(data) > 1:
                for i in data:
                    decryptedData.append(self.decodeStrAndReturn(i, shift))

                # Writes decrypted data to file
                writer.writeDataOverFile('DecodedData.txt', decryptedData)
                cleanData = self.takeAwayF('DecodedData.txt')
                writer.writeDataOverFile('DecodedData.txt', cleanData)
                print('Decoded data sent to DecodedData.txt!')
            else:
                # Writes decrypted data to file
                decryptedData.append(self.decodeStrAndReturn(data[0], shift))
                writer.writeDataOverFile('DecodedData.txt', decryptedData)
                cleanData = self.takeAwayF('DecodedData.txt')
                writer.writeDataOverFile('DecodedData.txt', cleanData)
                print('Decoded data sent to DecodedData.txt!')

        except TypeError:
            print('Error decrypting values')
        except IndexError:
            print('Error decrypting values')

    def takeAwayF(self, fileName):
        ''' Takes away the 'f' that appears at the end of decoded lines '''
        data = reader.getFileAllLines(fileName)

        if len(data) > 1:  # If there are multiple elements in the data
            for i in range(len(data)):  # loop through all data
                data[i] = data[i].replace("f\n", "")  # removes the 'f' at the end of strings
                if len(data[i]) == 0:  # if there are now empty entries in the data, remove them!
                    data.remove(data[i])
                    i -= 1  # after removing an entry, we need to move back a step (the list is now 1 shorter)
        else:  # If there's only one element in the data
            # To get rid of the last two characters
            string = data[0]
            wordList = list(string)  # Convert word to a list (each element is a character)
            maxLen = len(wordList)  # Get the total number of elements
            wordList.remove(wordList[maxLen - 1])  # Remove the last element (\n)
            wordList.remove(wordList[maxLen - 2])  # Remove the second to last element ('f')

            # Connects the characters into a single word
            word = ''
            for char in wordList:
                word += char

            data = [word]  # Adds the word into the data list

        return data


