import time, threading
from FileWrite import FileWrite


writer = FileWrite()

def performTask():
    writer.writeStringToFile('Output.txt', '' + str(time.ctime()) + '\n')
    threading.Timer(1, performTask).start()

performTask()

while True:
    data = input('Type in some value: ')