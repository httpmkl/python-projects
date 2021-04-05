import random

myCards = []
playCards = []
compCards = []
deck = []

def populateCards():
    for num in range(10):
        deck.append(f'RED {num}')
        deck.append(f'YELLOW {num}')
        deck.append(f'GREEN {num}')
        deck.append(f'BLUE {num}')

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

    startRound()

def startRound():
    gameOver = checkIfWon()

    if gameOver == 'Player':
        print('Game over! Player won')
    elif gameOver == 'Computer':
        print('Game over! Computer won')
    else:
        randCard = random.choice(deck)
        playCards.clear()
        print(randCard)

        print('\nYour Cards:')

        playableCards(randCard)
        putCardDown()

def checkIfWon():
    if len(myCards) == 0:
        return 'Player'
    elif len(compCards) == 0:
        return 'Computer'

def playableCards(card):
    deckCard = card.split(' ')

    counter = 1
    for i in myCards:
        # Checks if card is playable
        myCard = str(i).split(' ')
        if myCard[0] == deckCard[0]:
            canPlay = True
        elif myCard[1] == deckCard[1]:
            canPlay = True
        else:  # No similarities
            canPlay = False

        # Prints card
        if canPlay:
            print(f'{counter}. [ {i} ]')
            playCards.append(i)
        else:
            print(f'{counter}. {i}')

        counter += 1  # Updates counter

    if len(playCards) == 0:  # No playable cards
        choice = input('\n-> Press any key to draw a card!')
        drawCard(card)

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
                    myCards.remove(card)
                    deck.append(card)  # Returns card to deck so it doesn't run out
                    gaveInput = True
            else:
                print('\n-> Enter a valid input!')
        except ValueError:
            print('\n-> Enter a valid input!')

    startRound()

def drawCard(card):
    randCard = random.choice(deck)
    myCards.append(randCard)  # Adds card to your stack
    deck.remove(randCard)  # Removes card from deck
    playableCards(card)

handCards()