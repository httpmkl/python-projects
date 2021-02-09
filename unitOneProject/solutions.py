# GO THROUGH AND ADD MORE COMMENTS

inputReceive = False
onProblem = False
answered = False

# Question (to be used at the end of every solution)
def question():

    ques = int(input('\nWould you like to go back to the menu? \n1. Yes   \n2. No\n'))
    answered = True

    while answered:
        if ques > 2 or ques < 1:
            print('Please send a valid input!')
        elif ques == 1:
            print('\nRedirecting back to menu...\n')
            menu()
            answered = False
        elif ques == 2:
            print('\nI hope you enjoyed my project! Have a nice day :)')
            exit()  # or quit()? Let Mr. Rowell get back to me on this


# Problem 1: Casting
# Issues to later consider: Words -> int/float & float -> int are not possible
inputReceived = False

def problemOne():
    onProblem = True
    print('\nHello! Enter an input: ')
    userInput = input()
    inputReceived = True
    print('What would you like to convert this to?')

    while inputReceived and onProblem:
        choice = int(input('1. Float \n2. Int    \n3. String \n'))

        # In order to tell the user what they chose
        if choice == 1:
            typeChoice = 'Float'
        elif choice == 2:
            typeChoice = 'Int'
        elif choice == 3:
            typeChoice = 'String'

        # To check the validity of & process the input
        if choice > 3 or choice < 1:
            print('Invalid input! Please pick again')
        else:
            print(f'\nYou chose: {typeChoice} \nProcessing...')

            if choice == 1:
                print(f'-> {float(userInput)}')
                question()
            if choice == 2:
                print(int(userInput))
                question()
            if choice == 3:
                print(str(f"'{userInput}'"))
                question()


# Problem 2: Grade Calculator
def problemTwo():
    print('\nWelcome to the grade calculator!')

    score = int(input('\nEnter the score you got: '))
    overall = int(input('Now enter the total points: '))

    print('\nProcessing grade...    \n')
    inputReceived = True

    percentage = int(100 * score/overall)

    if percentage < 0:
        print('-> Are you sure you entered this correctly? Let\'s try again')
        problemTwo()
    else:
        print(f'-> Percentage: {percentage}%')

        if percentage > 100:
            print(f'-> Score: 8\nEither you got some bonus marks or you\'re lying to me!')
            question()
        elif percentage >= 95:
            print(f'-> Score: 8 \nWow! You must\'ve studied a lot')
            question()
        elif percentage >= 90:
            print(f'-> Score: 7 \nThat\'s fantastic!')
            question()
        elif percentage >= 85:
            print(f'-> Score: 6 \nGreat job!')
            question()
        elif percentage >= 80:
            print(f'-> Score: 5 \nNice!')
            question()
        elif percentage >= 75:
            print(f'-> Score: 4 \nNot bad :)')
            question()
        elif percentage >= 70:
            print(f'-> Score: 3 \nYou passed!')
            question()
        elif percentage >= 65:
            print(f'-> Score: 2 \nYou can do better!')
            question()
        elif percentage >= 50:
            print(f'-> Score: 1 \nStudy harder; you\'re about to fail!')
            question()
        else:
            print(f'-> Score: 0 \nAwh, better luck next time!')
            question()



# Problem 3: For Loops

# Problem 4: While Loops

# Problem 5: Finance Calculator

# Problem 6: Arrays & Lists

# Problem 7: Classes & Objects

# Menu
def menu():
    userChoice = int(input('Choose an option '))

    if userChoice == 1:
        problemOne()
    elif userChoice == 2:
        problemTwo()

# Ensures the program runs the menu upon starting
if not onProblem:
    menu()