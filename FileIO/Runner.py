'''

    TODO:
        - work on tier 3 + 1 extension problem
        - finish pt. 1 FileWrite exercise #3
        - fix the issue with decodeFromFile() (when a word has the letter 'f' in it)
            - clean up the function and takeAwayF() as well
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
