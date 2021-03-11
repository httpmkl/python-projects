from FileEncrypter import FileEncrypter
from FileRead import FileRead
from FileWrite import FileWrite
import random

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

    def decodeDataAndReturn(self, data, shift):
        ''' Decrypts a list of String using the given shift (and returns the list) '''
        shift *= -1
        decrypt = encrypt.encodeDataAndReturn(data, shift)
        return decrypt

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
                decryptedData = self.decodeDataAndReturn(data, shift)
            else:
                decryptedData.append(self.decodeStrAndReturn(data[0], shift))

            # Writes decrypted data to file
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

        for i in range(len(data)):  # loop through all data
            string = data[i]
            wordList = list(string)  # Convert word to a list (each element is a character)
            wordList.pop()  # Takes away last element in the array (\n)
            wordList.pop()  # Takes away the second to element in the array (letter)

            # Connects the characters into a single word
            word = ''
            for char in wordList:
                word += char

            data[i] = word  # Adds the word into the data list

        return data

    def bruteForceDecryption(self, fileName):
        ''' *DESC* '''
        data = reader.getFileAllLines(fileName)
        data = reader.removeNewlinesFromData(data)

        print("-> Type in the number of the successful encryption, or any other key if none are found")
        self.showDecryptTries(data)


    def showDecryptTries(self, data):
        ''' *DESC* '''
        count = 0
        rangeLen = 0
        decryptedData = []
        usedShift = []

        while rangeLen < 5:
            shift = random.randint(1, 10)
            if shift not in usedShift:
                rangeLen += 1
                usedShift.append(shift)
                decrypt = self.decodeDataAndReturn(data, shift)
                decryptedData.append(decrypt)
                count += 1
                print(f'{count}. {decrypt}')

        self.successOrTryAgain(count, data, decryptedData)

    def successOrTryAgain(self, count, data, decryptedData):
        ''' *DESC* '''
        userInput = input()
        try:
            userInput = int(userInput)
            if userInput > count or userInput < 1:
                print('\n-> Alright, here\'s are alternatives...')
                self.showDecryptTries(data)
            else:
                decrypt = decryptedData[userInput - 1]
                print('\n-> Success! Here is the decryption: \n')
                for i in decrypt:
                    print(i)
        except ValueError:
            print('\n-> Alright, here\'s are alternatives...')
            self.showDecryptTries(data)