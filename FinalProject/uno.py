import random

myCards = []
playCards = []
compCards = []
compPlayCards = []
deck = []
specialCards = []

def populateCards():
    for num in range(10):
        deck.append(f'RED {num}')
        deck.append(f'RED {num}')
        deck.append(f'YELLOW {num}')
        deck.append(f'YELLOW {num}')
        deck.append(f'GREEN {num}')
        deck.append(f'GREEN {num}')
        deck.append(f'BLUE {num}')
        deck.append(f'BLUE {num}')

    specialCards.append(f'RED +2')
    specialCards.append(f'RED +2')
    specialCards.append(f'YELLOW +2')
    specialCards.append(f'YELLOW +2')
    specialCards.append(f'GREEN +2')
    specialCards.append(f'GREEN +2')
    specialCards.append(f'BLUE +2')
    specialCards.append(f'BLUE +2')

    specialCards.append(f'RED SKIP')
    specialCards.append(f'RED SKIP')
    specialCards.append(f'YELLOW SKIP')
    specialCards.append(f'YELLOW SKIP')
    specialCards.append(f'GREEN SKIP')
    specialCards.append(f'GREEN SKIP')
    specialCards.append(f'BLUE SKIP')
    specialCards.append(f'BLUE SKIP')

    specialCards.append(f'RED REVERSE')
    specialCards.append(f'RED REVERSE')
    specialCards.append(f'YELLOW REVERSE')
    specialCards.append(f'YELLOW REVERSE')
    specialCards.append(f'GREEN REVERSE')
    specialCards.append(f'GREEN REVERSE')
    specialCards.append(f'BLUE REVERSE')
    specialCards.append(f'BLUE REVERSE')

    specialCards.append('WILD +4')
    specialCards.append('WILD +4')
    specialCards.append('WILD +4')
    specialCards.append('WILD +4')

    specialCards.append('WILD CARD')
    specialCards.append('WILD CARD')
    specialCards.append('WILD CARD')
    specialCards.append('WILD CARD')

    for i in specialCards:
        deck.append(i)

def intro():
    global gameplay
    print('\n[ Which mode of gameplay do you want? ]')

    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input('1. Beginner  2. Easy  3. Normal  \n'))
            if choice == 1:
                gameplay = 3
                gaveInput = True
            elif choice == 2:
                gameplay = 2
                gaveInput = True
            elif choice == 3:
                gameplay = 1
                gaveInput = True
            else:
                print('\n-> Choose from the options!')
        except ValueError:
            print('\n-> Enter a valid input!')

    handCards()

def handCards():
    # Adds cards to deck
    populateCards()

    for i in range(7):
        # Chooses 7 random cards for player
        randCard = random.choice(deck)
        myCards.append(randCard)  # Adds card to your stack
        deck.remove(randCard)  # Removes card from deck

    for i in range(7):
        # Chooses 7 random cards for computer
        randCard = random.choice(deck)
        compCards.append(randCard)  # Adds card to computer's stack
        deck.remove(randCard)  # Removes card from deck

    deckCard = []
    deckCard.append(random.choice(deck))
    startRound(deckCard)

def startRound(deckCard):
    playerTurn = True
    compTurn = False

    # Loop for alternating turns
    while playerTurn and not compTurn:
        gameOver = checkIfWon()
        if gameOver:
            break

        playCards.clear()
        lastCard = deckCard[len(deckCard) - 1]
        print(f'\nCard on deck: {lastCard}')

        print('\nYour Cards:')

        playableCards(lastCard)
        if len(playCards) != 0:
            putCardDown()
            deckCard.append(playedCard)

        playerTurn = False
        compTurn = True

        while compTurn and not playerTurn:
            gameOver = checkIfWon()
            if gameOver:
                break

            print('\n----------')

            compPlayCards.clear()
            lastCard = deckCard[len(deckCard) - 1]
            print(f'\nCard on deck: {lastCard}')

            compPlayableCards(lastCard)
            if len(compPlayCards) != 0:
                compPutCardDown()
                deckCard.append(compPlayedCard)

            print('\n----------')

            playerTurn = True
            compTurn = False

    if gameOver:
        if len(myCards) == 0:
            print('\n----------')
            print('\nGame over! Player won')
        elif len(compCards) == 0:
            print('\n----------')
            print('\nGame over! Computer won')


def checkIfWon():
    if len(myCards) == 0:
        return True
    elif len(compCards) == 0:
        return True
    else:
        return False

def playableCards(card):
    deckCard = str(card).split(' ')

    counter = 1
    for i in myCards:
        # Checks if card is playable
        myCard = str(i).split(' ')
        if myCard[0] == deckCard[0]:
            canPlay = True
        elif myCard[1] == deckCard[1]:
            canPlay = True
        elif myCard[0] == 'WILD':
            canPlay = True
        else:  # No similarities
            canPlay = False

        # Prints card
        if canPlay:
            if gameplay != 1:
                print(f'{counter}. [ {i} ]')
            else:  # Doesn't highlight playable cards w/ normal mode
                print(f'{counter}. {i}')
            playCards.append(i)
        else:
            print(f'{counter}. {i}')

        counter += 1  # Updates counter

    if len(playCards) == 0:  # No playable cards
        gaveInput = False
        while not gaveInput:
            choice = input('\n-> Press enter to draw a card!')
            if choice == '':  # Pressed enter
                gaveInput = True
                drawCard('Player', card)
            # If they don't press enter it just prompts them again


def compPlayableCards(card):
    deckCard = str(card).split(' ')

    for i in compCards:
        # Checks if card is playable
        compCard = str(i).split(' ')
        if compCard[0] == deckCard[0]:
            canPlay = True
        elif compCard[1] == deckCard[1]:
            canPlay = True
        else:  # No similarities
            canPlay = False

        # Prints card
        if canPlay:
            compPlayCards.append(i)

    if len(compPlayCards) == 0:  # No playable cards
        drawCard('Computer', card)

def putCardDown():
    gaveInput = False
    validCard = False

    while not gaveInput:
        try:
            choice = int(input('\n-> What card # would you like to play?  \n'))
            if 0 < choice <= len(myCards):
                card = myCards[choice - 1]
                # Checks for a valid card
                for i in playCards:
                    if card == i:
                        validCard = True  # Chosen card is playable

                if not validCard:  # Didn't choose a valid card
                    print('[ This is not a playable card! ]')
                else:  # Chose a valid card
                    print(f'[ PLAYED CARD: {card} ]')
                    playCard(card)
                    gaveInput = True
            else:
                print('\n-> Enter a valid input!')
        except ValueError:
            print('\n-> Enter a valid input!')

def playCard(card):
    global playedCard

    if card not in specialCards:
        myCards.remove(card)
        deck.append(card)  # Returns card to deck so it doesn't run out
        playedCard = card
    else:  # It's a special card
        myCards.remove(card)
        deck.append(card)  # Returns card to deck so it doesn't run out
        crd = card.split(' ')
        if crd[0] == 'WILD':
            wildCardPrompt()
            card = colour + 'CARD'
        playedCard = card
        specialCard()

def wildCardPrompt():
    global colour

    print('\n[ Which colour do you want to set the card to? ]')
    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input('1. Red  2. Blue  3. Yellow  3. Green  \n'))
            if choice == 1:
                colour = 'RED'
                gaveInput = True
            elif choice == 2:
                colour = 'BLUE'
                gaveInput = True
            elif choice == 3:
                colour = 'YELLOW'
                gaveInput = True
            elif choice == 4:
                colour = 'GREEN'
                gaveInput = True
            else:
                print('\n-> Choose from the options!')
        except ValueError:
            print('\n-> Enter a valid input!')

def specialCard():
    # TODO: special card moves
    pass

def compPutCardDown():
    global compPlayedCard

    card = random.choice(compPlayCards)
    print(f'[ PLAYED CARD: {card} ]')
    compCards.remove(card)
    deck.append(card)  # Returns card to deck so it doesn't run out
    compPlayedCard = card

def drawCard(type, card):
    if type == 'Player':
        randCard = getRandomCard(card)
        myCards.append(randCard)  # Adds card to your stack
        print('[ YOU DREW A CARD ]')
    elif type == 'Computer':
        randCard = random.choice(deck)
        compCards.append(randCard)  # Adds card to computer's stack
        print('[ THE COMPUTER DREW A CARD ]')

    deck.remove(randCard)  # Removes card from deck

def getRandomCard(card):
    if gameplay != 3:  # Normal or Easy mode
        drawnCard = random.choice(deck)
    else:  # Beginner
        matching = checkForMatching(card, deck)
        chance = random.randint(0, 10)
        if chance < 7:
            drawnCard = random.choice(matching)
        else:
            drawnCard = random.choice(deck)

    return drawnCard

def checkForMatching(card, deck):
    card = str(card).split(' ')
    matchingCards = []

    for i in range(len(deck)):
        deckCrd = str(deck[i]).split(' ')
        if card[0] == deckCrd[0]:
            matchingCards.append(str(deck[i]))
        elif card[1] == deckCrd[1]:
            matchingCards.append(str(deck[i]))
        else:
            pass

    return matchingCards

intro()