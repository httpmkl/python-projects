import datetime
from datetime import datetime as dt


class Bank:
    def __init__(self):
        pass

    def writeStringOverFile(self, fileName, stringData):
        ''' Write String data to file, overwriting previous file contents '''
        try:
            with open(fileName, 'w') as writer:
                writer.write(stringData)
        except IOError:
            print('Error writing to file: ', fileName)

    def readFirstLineFromFile(self, filename):
        ''' Print out the contents from the first line of a file '''
        try:
            with open(filename, 'r') as reader:
                data = reader.readline()
                return data
        except IOError:
            print('Unable to read from file: ', filename)

    def addSubtractMoney(self, account, amount):
        if account == "chequing":
            pastAmnt = self.readFirstLineFromFile("chequing.txt")
            currentAmnt = float(pastAmnt) + amount
            self.writeStringOverFile("chequing.txt", str(currentAmnt))
        if account == "savings":
            pastAmnt = self.readFirstLineFromFile("savings.txt")
            currentAmnt = float(pastAmnt) + amount
            self.writeStringOverFile("savings.txt", str(currentAmnt))

    def payWeek(self):
        day = dt.today().strftime('%Y %m %d')
        dayArray = day.split(" ")
        week = datetime.date(int(dayArray[0]), int(dayArray[1]), int(dayArray[2])).isocalendar().week

        isItPayWeek = self.readFirstLineFromFile("isItPayWeek.txt")
        payWeekInfo = isItPayWeek.split(" ")

        if float(payWeekInfo[0]) == week:
            if payWeekInfo[1] == "yes":
                return True
            elif payWeekInfo[1] == "no":
                return False
        else:
            weeks = week - float(payWeekInfo[0])

            if (payWeekInfo[1] == "yes" and weeks % 2 == 0) or (payWeekInfo[1] == "no" and weeks % 2 == 1):
                payWeekCurrentInfo = f"{str(week)} yes"
                self.writeStringOverFile("isItPayWeek.txt", payWeekCurrentInfo)
                self.payWeek()
            elif (payWeekInfo[1] == "no" and weeks % 2 == 0) or (payWeekInfo[1] == "yes" and weeks % 2 == 1):
                payWeekCurrentInfo = f"{str(week)} no"
                self.writeStringOverFile("isItPayWeek.txt", payWeekCurrentInfo)
                self.payWeek()

    def addToWeekSpending(self, amnt):
        day = dt.today().strftime('%Y %m %d')
        dayArray = day.split(" ")
        week = datetime.date(int(dayArray[0]), int(dayArray[1]), int(dayArray[2])).isocalendar().week

        isItThisWeek = self.readFirstLineFromFile("spending.txt")
        weekInfo = isItThisWeek.split(" ")

        if int(weekInfo[0]) == week:
            amount = float(weekInfo[1]) + amnt
            weekCurrentInfo = f"{str(week)} {amount}"
            self.writeStringOverFile("spending.txt", weekCurrentInfo)
        else:
            weekCurrentInfo = f"{str(week)} {amnt}"
            self.writeStringOverFile("spending.txt", weekCurrentInfo)

    def addToWeekEarning(self, amnt):
        day = dt.today().strftime('%Y %m %d')
        dayArray = day.split(" ")
        week = datetime.date(int(dayArray[0]), int(dayArray[1]), int(dayArray[2])).isocalendar().week

        isItThisWeek = self.readFirstLineFromFile("earnings.txt")
        weekInfo = isItThisWeek.split(" ")

        if int(weekInfo[0]) == week:
            amount = float(weekInfo[1]) + amnt
            weekCurrentInfo = f"{str(week)} {amount}"
            self.writeStringOverFile("earnings.txt", weekCurrentInfo)
        else:
            weekCurrentInfo = f"{str(week)} {amnt}"
            self.writeStringOverFile("earnings.txt", weekCurrentInfo)

    def getChequing(self):
        amnt = self.readFirstLineFromFile("chequing.txt")
        return amnt

    def getSavings(self):
        amnt = self.readFirstLineFromFile("savings.txt")
        return amnt

    def getSpending(self):
        roughAmnt = self.readFirstLineFromFile("spending.txt")
        amnt = roughAmnt.split(" ")
        amnt = amnt[1]
        return amnt

    def getEarnings(self):
        roughAmnt = self.readFirstLineFromFile("earnings.txt")
        amnt = roughAmnt.split(" ")
        amnt = amnt[1]
        return amnt