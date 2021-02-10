# GO THROUGH AND ADD MORE COMMENTS
import random

inputReceived = False
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
            exit()


# Problem 1: Casting
# Issues to later consider: Words -> int/float & float -> int are not possible
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
                print(f'-> {int(userInput)}')
                question()
            if choice == 3:
                print(f"-> '{str(userInput)}'")
                question()


# Problem 2: Grade Calculator
def problemTwo():
    onProblem = True

    print('\nWelcome to the grade calculator!')

    score = int(input('\nEnter your mark: '))
    overall = int(input('Now enter the total points: '))

    print('\nProcessing grade...    \n')
    inputReceived = True

    percentage = int(100 * score / overall)

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
def problemThree():
    print('\nWelcome to the range generator!  \n')

    inputLow = int(input('Enter the lowest integer in the range: '))
    inputHigh = int(input('Now enter the highest integer in the range: '))
    inputGap = int(input('Finally, what is the gap between the values: '))

    print('\nGenerating range...    \n')

    for num in range(inputLow, inputHigh, inputGap):
        print(num)
    else:
        print('\nSuccess! Range calculated')
        question()


# Problem 4: While Loops
def problemFour():
    lessThan50 = False
    greaterThan50 = False
    lessThan25 = False
    greaterThan25 = False
    lessThan75 = False
    greaterThan75 = False

    gotFirstHint = False
    gotSecondHint = False
    gotFinalHint = False

    isCorrect = False
    needHint = False

    print('\nHello! Welcome to the number guessing game')

    # Picks a random number between 1-100
    num = random.randint(1, 100)

    # Conditional loops to figure out where the number is located
    if num <= 25:
        lessThan50 = True
        lessThan25 = True
    elif num <= 50:
        lessThan50 = True
        greaterThan25 = True
    elif num <= 75:
        greaterThan50 = True
        lessThan75 = True
    else:
        greaterThan50 = True
        greaterThan75 = True

    # Guessing loop
    while not isCorrect and not needHint:
        guess = int(input('Insert your guess (between 1-100): '))

        if guess > 100 or guess < 0:
            print('\n-> Try again, but this time, between 1-10 \n')
        else:
            if guess == num:    # If guess is correct
                print('\n-> Wow, you guessed correctly! Congrats :)')
                question()
                isCorrect = True
                needHint = False
            else:   # If guess is incorrect
                needHint = True

        # First hint
        while needHint and not gotFirstHint:
            print('\nNot quite! Here\'s a hint:')

            if lessThan50:
                print('-> The number is less than or equal to 50    \n')
                needHint = False
                gotFirstHint = True
            else:
                print('-> The number is greater than 50 \n')
                needHint = False
                gotFirstHint = True

        # Second hint
        while needHint and not gotSecondHint:
            print('\nHuh, I guess the last hint wasn\'t very helpful. Here\'s another:')

            if lessThan25:
                print('-> The number is less than or equal to 25    \n')
                needHint = False
                gotSecondHint = True
            elif greaterThan25:
                print('-> The number is greater than 25    \n')
                needHint = False
                gotSecondHint = True
            elif lessThan75:
                print('-> The number is less than or equal to 75   \n')
                needHint = False
                gotSecondHint = True
            else:
                print('-> The number is greater than 75    \n')
                needHint = False
                gotSecondHint = True

        # Third hint
        while needHint and not gotFinalHint:
            print('\nIs it that difficult? Fine then, here\'s your final hint:')
            rangeLow = num - random.randint(2, 4)
            rangeHigh = num + random.randint(2, 4)
            print(f'-> The number is somewhere between {rangeLow} and {rangeHigh}    \n')
            needHint = False
            gotFinalHint = True

        # Said if final hint has already been given
        while needHint and gotFinalHint:
            print('So close! Try again')
            needHint = False


# Problem 5: Finance Calculator
def problemFive():
    print('Under construction')


# Problem 6: Arrays & Lists
def problemSix():
    print('Under construction')


# Problem 7: Classes & Objects


# Menu
def menu():
    userChoice = int(input('Choose an option '))

    if userChoice == 1:
        problemOne()
    elif userChoice == 2:
        problemTwo()
    elif userChoice == 3:
        problemThree()
    elif userChoice == 4:
        problemFour()
    elif userChoice == 5:
        problemFive()
    elif userChoice == 6:
        problemSix()
    else:
        print('Sorry, that is not an option available!')
        menu()


# Ensures the program runs the menu upon starting
if not onProblem:
    menu()
