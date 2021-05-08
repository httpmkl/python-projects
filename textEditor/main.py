'''

    Ayup??

'''
import string
from FileRead import FileRead


def menu():
    print('\n[ TEXT EDITOR - Spelling corrections at the click of a button! ]')
    print('-> Enter your text and a corrected version will be printed!')
    print('\n-------------------\n')

    rawText = input('')
    checkForErrors(rawText)


def checkForErrors(rawText):
    filteredText = separateWordsProperly(rawText)
    print(filteredText)


def separateWordsProperly(rawText):
    words = rawText.split()
    letters = []
    alphabet = getAlphabet()
    filteredText = ''

    for i in words:
        word = []
        for j in i:
            word.append(j)
        letters.append(word)


    for num in range(len(letters)):
        i = list(letters[num])
        for j in range(len(i)):
            if i[j] not in alphabet:
                letters[num].remove(i[j])


    for i in letters:
        word = ''
        for j in i:
            word += j
        word += ' '
        filteredText += word

    return filteredText  # Text without punctuation


def getAlphabet():
    lowerLetters = string.ascii_lowercase
    upperLetters = string.ascii_uppercase

    alphabet = []
    for i in lowerLetters:
        alphabet.append(i)
    for i in upperLetters:
        alphabet.append(i)

    return alphabet

def getDictionaryWords():
    dictionary = FileRead.getFileAllLines(FileRead, 'AllWords.txt')

    for i in range(len(dictionary)):
        rawWord = dictionary[i]
        cleanWord = rawWord.split('\n')
        dictionary[i] = cleanWord[0]

    return dictionary


def testForAccuracy(incWords):
    dictionary = getDictionaryWords()
    for num in range(len(dictionary)):
        word = dictionary[num]
        dictionary[num] = word.lower()

    for i in incWords:
        lettersOne = list(i)
        for j in dictionary:
            lettersTwo = list(j)

            try:
                matchingLetters = 0
                for num in range(len(lettersOne)):
                    letterOne = lettersOne[num]
                    letterTwo = lettersTwo[num]
                    if letterOne.lower() == letterTwo.lower():
                        matchingLetters += 1
            except IndexError:
                pass

            if len(lettersOne) <= 10:
                diff = 1
            else:
                diff = 2

            maxLetters = len(lettersOne) + diff
            minLetters = len(lettersOne) - diff

            if len(lettersOne) == len(lettersTwo):
                if maxLetters >= matchingLetters >= minLetters:
                        print(i)
                        print(j)
                        print()


incWords = ['wondeing', 'hetlo', 'hapxy', 'abuut', 'welcone']
#testForAccuracy(incWords)
menu()