from Messages3 import ChatBot

chatBot = ChatBot('Elon')
chatBot.printAIName()
print(chatBot.myName)

chatBot.rememberMyName('Nora')
print(chatBot.myName)

chatBotTwo = ChatBot('Bezos')
chatBotTwo.printAIName()
print(chatBotTwo.myName)


# 'Placeholder' was a class variable; the same for both objects
# Changing class variables for one instance = changes for ALL instances
# 'Elon' and 'Bezos' was an instance variable; specific to the object


