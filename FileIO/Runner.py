from FileRead import FileRead
from FileWrite import FileWrite
from FileEncrypter import FileEncrypter
from FileDecrypter import FileDecrypter

reader = FileRead()
writer = FileWrite()

reader.numOfLinesInFile('AllWords.txt')
reader.numOfLinesInFile('AllWords.txt')
reader.numOfCharactersInFile('AllWords.txt')
reader.checkIfFileHasPhrase('AllWords.txt', 'absent')
reader.returnWordsOfLength('AllWords.txt', '1')