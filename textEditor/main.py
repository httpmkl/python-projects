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
    filText = str(filteredText)
    samp = filText.split(' ')
    samp.pop()
    print(samp)


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
    corWords = []
    dictionary = getDictionaryWords()
    for num in range(len(dictionary)):
        word = dictionary[num]
        dictionary[num] = word.lower()

    for i in incWords:
        options = []
        for j in dictionary:
            if i.lower() != j.lower():
                lettersOne = list(i)
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

                if len(lettersOne) <= 13:
                    diff = 1
                else:
                    diff = 2

                maxLetters = len(lettersOne) + diff
                minLetters = len(lettersOne) - diff

                if len(lettersOne) == len(lettersTwo):
                    if maxLetters >= matchingLetters >= minLetters:
                        options.append(j)
            else:
                options.clear()
                options.append('1')
                options.append(j)

        if options[0] == '1':
            answer = options[1]
            options.clear
            options.append(answer)

        corWords.append(options)

    print(incWords)
    print(corWords)


incWords = ['wondeing', 'there', 'hetlo', 'hapxy', 'abuut', 'welcone']
testForAccuracy(incWords)
# menu()
