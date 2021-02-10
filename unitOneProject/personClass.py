class Person:
    def __init__(self, myName, myAge, favQuote):
        self.myName = myName
        self.myAge = myAge
        self.favQuote = favQuote

    def getMyName(self):
        return self.myName

    def getMyAge(self):
        return self.myAge

    def getFavQuote(self):
        return self.favQuote