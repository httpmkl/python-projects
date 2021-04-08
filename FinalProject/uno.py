'''

    What I added:
        - All of the basic UNO gameplay mechanics
        - The ability to play against the computer
        - UN0's special cards (Wild (card & +4), +2, reverse, skip)
            - The computer's ability to use special cards
        - Different modes of gameplay (beginner/easy/normal)

    What I need to add:
        TODO: POPULATE CARDS.PY AND PLAYER.PY
        -> gameplay development:
            - The ability to stack special cards to avoid picking up
            - Unique special cards (that are not in UNO)
        -> extended:
            - Save/load game abilities
            - Multiplayer options (multiple people on the same device)
                - Team mode for even numbers
            - Menu screen to contain & organize these features
        -> general reminders:
            - Improve the reverse card mechanics when multiplayer is introduced
            - Ensure everything is modular & organized before submitting

'''

import random
from cards import Cards

myCards = []
playCards = []
compCards = []
compPlayCards = []
specialCards = []

skippedTurn = []
userSkip = []
reversedTurn = []
userReverse = []


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
    cards.populateCards()

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

    deckCard = [random.choice(deck)]
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
        userSkip.clear()
        userReverse.clear()

        while compTurn and not playerTurn:
            gameOver = checkIfWon()
            if gameOver:
                break

            print('\n----------')

            compPlayCards.clear()
            lastCard = deckCard[len(deckCard) - 1]
            print(f'\nCard on deck: {lastCard}')

            if len(skippedTurn) == 0 and len(reversedTurn) == 0:
                compPlayableCards(lastCard)

                if len(compPlayCards) != 0:
                    compPutCardDown()
                    deckCard.append(compPlayedCard)

            elif len(skippedTurn) != 0 and len(reversedTurn) == 0:  # Their turn has been skipped
                print('THEIR TURN HAS BEEN SKIPPED!')
                skippedTurn.clear()

            elif len(skippedTurn) == 0 and len(reversedTurn) != 0:  # The order has been reversed
                # On 2 player games, reverse works as a skip
                print('THE ORDER HAS BEEN REVERSED!')
                reversedTurn.clear()

            print('\n----------')

            playerTurn = True
            compTurn = False

    if gameOver:
        if len(myCards) == 0:
            print('\n----------')
            print('\nGame over! Player won')
        elif len(compCards) == 0:
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

    # TODO: Put some of this in cards.py

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

    if len(userSkip) != 0 or len(userReverse) != 0:
        playCards.clear()

    if len(playCards) == 0:  # No playable cards
        gaveInput = False
        while not gaveInput:
            if len(userReverse) == 0 and len(userSkip) != 0:
                choice = input('\n-> Your turn has been skipped! Press enter to continue')
                if choice == '':  # Pressed enter
                    gaveInput = True
            elif len(userSkip) == 0 and len(userReverse) != 0:
                choice = input('\n-> The order has been reversed! Press enter to continue')
                if choice == '':  # Pressed enter
                    gaveInput = True
            else:
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
                    playCard(card)
                    print(f'[ PLAYED CARD: {card} ]')
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
        specialCard(card)
        if crd[0] == 'WILD':
            wildCardPrompt()
            card = colour + ' CARD'
        playedCard = card


def wildCardPrompt():
    global colour

    print('\n[ Which colour do you want to set the card to? ]')
    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input('1. Red | 2. Blue | 3. Yellow | 4. Green  \n'))
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


def specialCard(card):
    crd = card.split(' ')
    move = crd[1]

    if move == '+4':  # Wild +4
        for i in range(4):
            randCard = random.choice(deck)
            compCards.append(randCard)  # Adds card to computer's stack
            deck.remove(randCard)  # Removes card from deck
        skippedTurn.append('skip')  # Skips turn
    elif move == '+2':  # Colour +2
        for i in range(2):
            randCard = random.choice(deck)
            compCards.append(randCard)  # Adds card to computer's stack
            deck.remove(randCard)  # Removes card from deck
        skippedTurn.append('skip')  # Skips turn
    elif move == 'SKIP':  # Colour skip
        skippedTurn.append('skip')
    elif move == 'REVERSE':  # Colour reverse
        reversedTurn.append('reverse')

    # Nothing happens for wild cards; only changes colour


def compPutCardDown():
    card = random.choice(compPlayCards)
    compPlayCard(card)
    print(f'[ PLAYED CARD: {card} ]')


def compPlayCard(card):
    global compPlayedCard

    if card not in specialCards:
        compCards.remove(card)
        deck.append(card)  # Returns card to deck so it doesn't run out
        compPlayedCard = card
    else:  # It's a special card
        compCards.remove(card)
        deck.append(card)  # Returns card to deck so it doesn't run out
        crd = card.split(' ')
        compSpecialCard(card)
        if crd[0] == 'WILD':
            col = compWildCard()
            card = col + ' CARD'
        compPlayedCard = card


def compWildCard():
    choice = random.randint(1, 5)

    if choice == 1:
        col = 'RED'
    elif choice == 2:
        col = 'BLUE'
    elif choice == 3:
        col = 'YELLOW'
    elif choice == 4:
        col = 'GREEN'

    return col


def compSpecialCard(card):
    crd = card.split(' ')
    move = crd[1]

    if move == '+4':  # Wild +4
        for i in range(4):
            randCard = random.choice(deck)
            myCards.append(randCard)  # Adds card to player's stack
            deck.remove(randCard)  # Removes card from deck
        userSkip.append('skip')  # Skips turn
    elif move == '+2':  # Colour +2
        for i in range(2):
            randCard = random.choice(deck)
            myCards.append(randCard)  # Adds card to player's stack
            deck.remove(randCard)  # Removes card from deck
        userSkip.append('skip')  # Skips turn
    elif move == 'SKIP':  # Colour skip
        userSkip.append('skip')
    elif move == 'REVERSE':  # Colour reverse
        userReverse.append('reverse')


def drawCard(user, card):
    if user == 'Player':
        randCard = cards.getRandomCard(card, gameplay)
        myCards.append(randCard)  # Adds card to your stack
        print('[ YOU DREW A CARD ]')
        skippedTurn.clear()
        reversedTurn.clear()
    elif user == 'Computer':
        randCard = random.choice(deck)
        compCards.append(randCard)  # Adds card to computer's stack
        print('[ THE COMPUTER DREW A CARD ]')
        userSkip.clear()
        userReverse.clear()

    deck.remove(randCard)  # Removes card from deck


cards = Cards()
deck = cards.deck
specialCards = cards.specialCards

intro()
