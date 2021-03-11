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
            cleanData = self.takeAwayExtraCharacters('DecodedData.txt')
            writer.writeDataOverFile('DecodedData.txt', cleanData)
            print('Decoded data sent to DecodedData.txt!')

        except TypeError:
            print('Error decrypting values')
        except IndexError:
            print('Error decrypting values')

    def takeAwayExtraCharacters(self, fileName):
        ''' Takes away the extra characters that appears at the end of decoded lines '''
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
        data = reader.getFileAllLines(fileName)
        data = reader.removeNewlinesFromData(data)

        print("-> Testing decryptions...")
        self.showDecryptTries(data)


    def showDecryptTries(self, data):
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
                # To show only a sample of the data
                sample = []
                try:
                    for i in range(3):
                        sample.append(decrypt[i])
                except IndexError:
                    pass
                print(f'{count}. {sample}')

        self.divideToWords(data, decryptedData)

    def divideToWords(self, data, decryptedData):
        separator = ' '
        attempt = 0

        for i in decryptedData:
            if attempt == 0:
                string = separator.join(i)
                guessOne = string.split()
                attempt += 1
            elif attempt == 1:
                string = separator.join(i)
                guessTwo = string.split()
                attempt += 1
            elif attempt == 2:
                string = separator.join(i)
                guessThree = string.split()
                attempt += 1
            elif attempt == 3:
                string = separator.join(i)
                guessFour = string.split()
                attempt += 1
            elif attempt == 4:
                string = separator.join(i)
                guessFive = string.split()

        self.checkForSuccess(data, decryptedData, guessOne, guessTwo, guessThree, guessFour, guessFive)

    def checkForSuccess(self, data, decryptedData, guessOne, guessTwo, guessThree, guessFour, guessFive):
        dictionary = reader.getFileAllLines('AllWords.txt')
        dictionary = reader.removeNewlinesFromData(dictionary)

        success = False
        oneCorrect = False
        twoCorrect = False
        threeCorrect = False
        fourCorrect = False
        fiveCorrect = False
        realWords = 0

        while not success:
            for i in guessOne:
                for word in dictionary:
                    if i.lower() == word.lower():
                        realWords += 1
                        if realWords >= (len(guessOne)*0.8):
                            oneCorrect = True
                            success = True
                            break

            for i in guessTwo:
                for word in dictionary:
                    if i.lower() == word.lower():
                        realWords += 1
                        if realWords >= (len(guessTwo) * 0.8):
                            twoCorrect = True
                            success = True
                            break

            for i in guessThree:
                for word in dictionary:
                    if i.lower() == word.lower():
                        realWords += 1
                        if realWords >= (len(guessThree) * 0.8):
                            threeCorrect = True
                            success = True
                            break

            for i in guessFour:
                for word in dictionary:
                    if i.lower() == word.lower():
                        realWords += 1
                        if realWords >= (len(guessFour) * 0.8):
                            fourCorrect = True
                            success = True
                            break

            for i in guessFive:
                for word in dictionary:
                    if i.lower() == word.lower():
                        realWords += 1
                        if realWords >= (len(guessFive) * 0.8):
                            fiveCorrect = True
                            success = True
                            break
            if not success:
                success = True
                print('\n-> I guess there weren\'t any correct decryptions. We\'ll try again...')
                self.showDecryptTries(data)

        self.reportCorrectAnswer(decryptedData, oneCorrect, twoCorrect, threeCorrect, fourCorrect, fiveCorrect)

    def reportCorrectAnswer(self, decryptedData, one, two, three, four, five):
        if one:
            print('\n-> Eureka! We found a successful decryption')
            guess = decryptedData[0]
            print(guess)
        elif two:
            print('\n-> Eureka! We found a successful decryption')
            guess = decryptedData[1]
            print(guess)
        elif three:
            print('\n-> Eureka! We found a successful decryption')
            guess = decryptedData[2]
            print(guess)
        elif four:
            print('\n-> Eureka! We found a successful decryption')
            guess = decryptedData[3]
            print(guess)
        elif five:
            print('\n-> Eureka! We found a successful decryption')
            guess = decryptedData[4]
            print(guess)