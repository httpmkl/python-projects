# GO THROUGH AND ADD MORE COMMENTS
import random
from personClass import Person
onProblem = False

# Question (to be used at the end of every solution)
def question():
    ques = int(input('\nWould you like to go back to the menu? \n1. Yes   \n2. No\n'))
    answered = True

    while answered:
        if ques > 2 or ques < 1:
            print('\n-> Please enter a valid input!')
            question()
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
    print('\nWelcome to the value converter!')
    userInput = input('\nEnter an input: ')

    inputReceived = True
    print('\nWhat would you like to convert this to?')

    while inputReceived:
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

            if choice == 1: # Chose float
                print(f'-> {float(userInput)}')
                question()
            elif choice == 2: # Chose int
                print(f'-> {int(userInput)}')
                question()
            else: # Chose string
                print(f"-> '{str(userInput)}'")
                question()


# Problem 2: Conditional Logic
def problemTwo():
    onProblem = True

    print('\nWelcome to the grade calculator!')

    score = int(input('\nEnter your mark: '))
    overall = int(input('Now enter the total points: '))

    print('\nProcessing grade...    \n')
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
    print('\nWelcome to the range generator!    \n')

    inputLow = int(input('Enter the lowest integer in the range: '))
    inputHigh = int(input('Now enter the highest integer in the range: '))
    inputGap = int(input('Finally, enter the gap between the values: '))

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

    print('\nWelcome to the number guessing game!   \n')

    # Picks a random number between 1-100
    num = random.randint(1, 100)

    # Conditional loops to figure out where the number is located
    if num <= 25:
        lessThan25 = True
        lessThan50 = True
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
            print('\n-> Try again, but this time, between 1-100 \n')
        else:
            if guess == num:  # If guess is correct
                print('\n-> Wow, you guessed correctly! Congrats :)')
                question()
                isCorrect = True
                needHint = False
            else:  # If guess is incorrect
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


# Problem 5: Operators
def problemFive():
    choseOption = False
    wantsToContinue = True

    print('\nWelcome to the finance calculator!')

    while not choseOption:
        print('\nWhat service would you like to use?')
        choice = int(input('1. Calculate cost after tax   \n2. Calculate how many items I can buy   \n'))

        if choice > 2 or choice < 1:
            print('\n-> Invalid input! Please pick again')
        else:
            choseOption = True

        while choseOption and wantsToContinue:

            if choice == 1:
                ogCost = float(input('\nEnter the cost of the item: '))
                tax = int(input('Now enter the tax percentage: '))

                cost = (ogCost * tax / 100) + ogCost
                print(f'\nThe total cost is:')
                print('-> ${:.2f}'.format(cost))  # Brings the value to 2 decimal spaces
                wantsToContinue = False
            else:
                balance = float(input('\nEnter your current bank balance: '))
                cost = float(input('Now enter the total cost of the item: '))

                leftOver = balance % cost
                amount = int((balance - leftOver) / cost)
                print(f'\nYou can purchase: \n-> {amount} item(s)')
                print('Money left over:')
                print('-> ${:.2f}'.format(leftOver))
                wantsToContinue = False

        while not wantsToContinue:
            print('\nDo you still need to use the finance calculator?')
            choiceTwo = int(input('1. Yes, take me to the options   \n2. No, I\'m done here \n'))

            if choiceTwo > 2 or choiceTwo < 1:
                print('\n-> Invalid input! Please pick again')
            elif choiceTwo == 1:
                wantsToContinue = True
                choseOption = False
            else:
                question()


# Problem 6: Arrays & Lists
def problemSix():
    finished = False
    print('\nWelcome to the data organizer!')
    print("Enter each number one at a time, and type 'end' when finished in order to see the list\'s attributes!   \n")

    data = []

    while not finished:
        value = input('-> ')

        if value == 'end' or value == "'end'": # The "'end'" is in case they type in 'end' with the quotations
            finished = True
            low = min(data)
            high = max(data)
            average = int(sum(data) / len(data))

            print(f'\nLowest value: {low}')
            print(f'Highest value: {high}')
            print(f'Average value: {average}')
            question()
        else:
            value = int(value)
            data.append(value)


# Problem 7: Classes & Objects
def problemSeven():
    print('\nWelcome! Create your profile below')
    needToEdit = True

    while needToEdit:
        userName = str(input('\nEnter your name: '))
        userAge = int(input('Enter your age: '))
        userQuote = str(input('Enter your favourite quote: '))
        person = Person(userName, userAge, userQuote)
        needToEdit = False

        print('\nPROFILE')
        print(f'Name: {person.getMyName()}')
        print(f'Age: {person.getMyAge()}')
        print(f'Favourite quote: "{person.getFavQuote()}"')

        print('\nWould you like to edit your profile?')
        choice = int(input('1. Yes  \n2. No \n'))

        if choice > 2 or choice < 1:
            print('\n-> Invalid input! Please pick again')
        elif choice == 1:
            needToEdit = True
        else:
            print(f'\n-> Profile set for {person.getMyName()}!')
            question()


# Menu
def menu():
    print('OPTIONS')
    print('1. Value Converter   2. Grade Calculator   3. Range Generator')
    print('4. Guessing Game   5. Finance Calculator   6. Data Organizer \n7. Profile Creator')
    userChoice = int(input('\nEnter your selection: '))

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
    elif userChoice == 7:
        problemSeven()
    else:
        print('\nSorry, that is not an option available!    \n')
        menu()


# Ensures the program runs the menu upon starting
if not onProblem:
    print('\nHello user! Welcome to my program  \n')
    menu()
