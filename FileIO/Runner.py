'''

    TODO:
        - work on an extension problem
        - finish pt. 1 FileWrite exercise #3
        - clean up the decodeFromFile() and takeAwayF()
        - ensure all of the code is modular and generalized

'''


from FileRead import FileRead
from FileWrite import FileWrite
from FileEncrypter import FileEncrypter
from FileDecrypter import FileDecrypter


reader = FileRead()
writer = FileWrite()
encrypt = FileEncrypter()
decrypt = FileDecrypter()
print()

# encrypt.randomizedEncrypter('fileOne.txt')
decrypt.bruteForceDecryption('EncodedData.txt')