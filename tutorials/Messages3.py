# Class = blueprint
# Instance = object; the implemented class

class ChatBot:
    # Class variables — same value for EVERY OBJECT
    myName = 'Placeholder'

    def __init__(self, aiName):
        # print('ChatBot class created!')
        self.aiName = aiName # Instance variables

    def printMyName(self):
        # print(myName)
        print('No name yet...')

    def printAIName(self):
        print(self.aiName)

    def rememberMyName(self, name):
        ChatBot.myName = name
        # Accessing the class variable to make changes