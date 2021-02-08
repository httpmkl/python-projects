# Python classes and modules
from Messages2 import ChatBot
import Messages2

chatBot = ChatBot()  # Instantiation

chatBot.printMessage()
chatBot.sayHiToMe('Nora')
print(chatBot.sendSecretMessage())
print(chatBot.doMyHomework(6, 2))
print(chatBot.doMyHomework(7, 3))

# Outside of class; no longer chatBot
print(Messages2.nonSentientMessage())