from FileWrite import FileWrite
from FileRead import FileRead
import random

reader = FileRead()
writer = FileWrite()

class FileEncrypter:

    def __init__(self):
        pass

    def characterCast(self, character):
        return ord(character)

    def convertBackToChar(self, number):
        return chr(number)

    def encodeString(self, message, key):
        ''' Change the value of the String using the given key and a Cesarean cipher (prints + returns the value) '''
        encryptedString = ''

        messageList = list(message)

        for character in messageList:
            intVal = ord(character)
            shift = intVal + key
            # so the shift doesn't exceed 126 or go below 32
            if shift > 126:
                shift = 31 + (shift - 126)
            elif shift < 32:
                shift = 127 + (shift - 32)
            else:
                pass
            newChar = chr(shift)
            encryptedString += newChar

        print("Encrypted message: " + encryptedString)
        return encryptedString

    def encodeStrAndReturn(self, message, key):
        ''' Change the value of the String using the given key and a Cesarean cipher (only returns the value) '''
        encryptedString = ''

        messageList = list(message)

        for character in messageList:
            intVal = ord(character)
            shift = intVal + key
            # so the shift doesn't exceed 126 or go below 32
            if shift > 126:
                shift = 31 + (shift - 126)
            elif shift < 32:
                shift = 127 + (shift - 32)
            else:
                pass
            newChar = chr(shift)
            encryptedString += newChar

        return encryptedString

    def encodeData(self, strings, key):
        ''' Change the value of the list of Strings using the given key and a Cesarean cipher (prints + returns the values) '''
        data = list(strings)  # to ensure the format is a list
        encryptedData = []

        try:
            for i in data:
                encryptedData.append(self.encodeStrAndReturn(i, key))

            print('Encrypted values:')
            for i in encryptedData:
                print(f'-> {i}')

            return encryptedData

        except TypeError:
            print('Error encrypting values; please ensure all elements are strings!')

    def encodeDataAndReturn(self, strings, key):
        ''' Change the value of the list of Strings using the given key and a Cesarean cipher (only returns the values) '''
        data = list(strings)  # to ensure the format is a list
        encryptedData = []

        try:
            for i in data:
                encryptedData.append(self.encodeStrAndReturn(i, key))

            return encryptedData

        except TypeError:
            print('Error encrypting values; please ensure all elements are strings!')

    def encodeToFile(self, strings, key):
        ''' Encodes given data using the key and adds it to a custom file '''

        data = []
        if type(strings) == list:
            # If a list is given, it becomes the data list
            data = strings
        else:
            # If a single string is given, it's added to the data list as a single token
            data.append(strings)

        data = reader.removeNewlinesFromData(data)
        encryptedData = []

        try:
            if len(data) > 1:  # If there are multiple elements in the list
                for i in data:
                    encryptedData.append(self.encodeStrAndReturn(i, key))  # Encrypts then adds to encrypted data list

                writer.writeDataOverFile('EncodedData.txt', encryptedData)  # Adds encrypted data to EncodedData.txt
                print('Encrypted data sent to EncodedData.txt! \n')

            else:  # If there is only one element
                encryptedData.append(self.encodeStrAndReturn(data[0], key))  # Encrypts then adds to encrypted data list
                writer.writeDataOverFile('EncodedData.txt', encryptedData)  # Adds encrypted data to EncodedData.txt
                print('Encrypted data sent to EncodedData.txt! \n')

        except TypeError:
            print('Error encrypting values; please ensure all elements are strings!')
        except IndexError:
            print('Error encrypting values; please ensure all elements are strings!')

    def randomizedEncrypter(self, fileName):
        ''' Randomly generates a cypher to apply to the given file sends the encrypted data to another file '''

        data = reader.getFileAllLines(fileName)
        key = random.randint(1, 10)
        self.encodeToFile(data, key)