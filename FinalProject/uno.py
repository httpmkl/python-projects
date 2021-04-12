'''

    What I added:
        - All of the basic UNO gameplay mechanics
        - The ability to play against the computer
        - UN0's special cards (Wild (card & +4), +2, reverse, skip)
            - The computer's ability to use special cards
        - Different modes of gameplay (beginner/easy/normal)
        - Multiplayer options (to an extent)

    What I need to add/do:
        - Generalize player functions to adapt to computer plays
            - (add conditional variables in the parenthesis to distinguish between the types)
        - Improve reverse mechanics
        - The ability to stack special cards to avoid picking up
        - Unique special cards (that are not in UNO)
        - Save/load game abilities
        - Team mode for even numbers (in multiplayer)
        - Menu screen to contain & organize these features
        - Ensure everything is modular & organized before submitting

'''

import random
from cards import Cards
from player import Player
from player import Computer

myCards = []
compCards = []

skippedTurn = []
reversedTurn = []


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

    for i in players:
        for num in range(7):
            # Chooses 7 random cards for player
            randCard = random.choice(deck)
            i.myCards.append(randCard)  # Adds card to stack
            deck.remove(randCard)  # Removes card from deck

    deckCard = [random.choice(deck)]
    startRound(deckCard)

def startRound(deckCard):
    global playCards, compPlayCards

    for i in players:
        type = i.myName.split(' ')
        type = type[0]

        if type.lower() == 'player':
            lastCard = deckCard[len(deckCard) - 1]
            print(f'\nCard on deck: {lastCard}')

            print(f'\n{i.myName} Cards:')

            playableCards(i, lastCard)
            if len(playCards) != 0:
                for num in range(len(players)):
                    if i == players[num]:
                        next = num + 1
                try:
                    putCardDown(i, players[next])
                except IndexError:
                    putCardDown(i, players[0])
                deckCard.append(playedCard)
                playCards.clear()

            print('\n----------')

        else:
            lastCard = deckCard[len(deckCard) - 1]
            print(f'\nCard on deck: {lastCard}')

            if len(skippedTurn) == 0 and len(reversedTurn) == 0:
                compPlayableCards(i, lastCard)

                if len(compPlayCards) != 0:
                    for num in range(len(players)):
                        if i == players[num]:
                            next = num + 1
                    try:
                        compPutCardDown(players[next])
                    except IndexError:
                        compPutCardDown(players[0])
                    deckCard.append(compPlayedCard)

                compPlayCards.clear()

            elif len(skippedTurn) != 0 and len(reversedTurn) == 0:  # Their turn has been skipped
                print('THEIR TURN HAS BEEN SKIPPED!')
                skippedTurn.clear()

            elif len(skippedTurn) == 0 and len(reversedTurn) != 0:  # The order has been reversed
                # On 2 player games, reverse works as a skip
                print('THE ORDER HAS BEEN REVERSED!')
                reversedTurn.clear()

            print('\n----------')

        playersWon = checkIfWon()
        if len(playersWon) > 0:
            gameOver(type, playersWon[0])

        if i == players[len(players) - 1]:  # Last player
            startRound(deckCard)


def gameOver(type, player):
        if type.lower() == 'player':
            print(f'\nGame over! {player} won')
            quit()
        else:
            print('\nGame over! Computer won')
            quit()


def checkIfWon():
    playersWon = []
    for i in players:
        if len(i.myCards) == 0:
            playersWon.append(i.myName)

    return playersWon


def playableCards(player, card):
    global playCards

    deckCard = str(card).split(' ')
    cards.playableCards(player.myCards, deckCard)
    playCards = cards.playCards

    counter = 1
    for i in player.myCards:
        # Prints card
        if i in playCards:
            if gameplay != 1:
                print(f'{counter}. [ {i} ]')
            else:  # Doesn't highlight playable cards w/ normal mode
                print(f'{counter}. {i}')
        else:
            print(f'{counter}. {i}')

        counter += 1  # Updates counter

    if len(skippedTurn) != 0 or len(reversedTurn) != 0:
        playCards.clear()

    if len(playCards) == 0:  # No playable cards
        gaveInput = False
        while not gaveInput:
            if len(reversedTurn) == 0 and len(skippedTurn) != 0:
                choice = input('\n-> Your turn has been skipped! Press enter to continue')
                if choice == '':  # Pressed enter
                    gaveInput = True
                    skippedTurn.clear()
            elif len(skippedTurn) == 0 and len(reversedTurn) != 0:
                choice = input('\n-> The order has been reversed! Press enter to continue')
                if choice == '':  # Pressed enter
                    gaveInput = True
                    reversedTurn.clear()
            else:
                choice = input('\n-> Press enter to draw a card!')
                if choice == '':  # Pressed enter
                    gaveInput = True
                    drawCard('Player', player, card)
                # If they don't press enter it just prompts them again


def compPlayableCards(player, card):
    global compPlayCards

    deckCard = str(card).split(' ')
    cards.playableCards(compCards, deckCard)
    compPlayCards = cards.playCards

    if len(compPlayCards) == 0:  # No playable cards
        drawCard('Computer', player, card)


def putCardDown(player, nextPlayer):
    gaveInput = False
    validCard = False

    while not gaveInput:
        try:
            choice = int(input('\n-> What card # would you like to play?  \n'))
            if 0 < choice <= len(player.myCards):
                card = player.myCards[choice - 1]
                # Checks for a valid card
                for i in playCards:
                    if card == i:
                        validCard = True  # Chosen card is playable

                if not validCard:  # Didn't choose a valid card
                    print('[ This is not a playable card! ]')
                else:  # Chose a valid card
                    playCard(player, card, nextPlayer)
                    print(f'[ PLAYED CARD: {card} ]')
                    gaveInput = True
            else:
                print('\n-> Enter a valid input!')
        except ValueError:
            print('\n-> Enter a valid input!')


def playCard(player, card, nextPlayer):
    global playedCard

    if card not in specialCards:
        player.myCards.remove(card)
        deck.append(card)  # Returns card to deck so it doesn't run out
        playedCard = card
    else:  # It's a special card
        player.myCards.remove(card)
        deck.append(card)  # Returns card to deck so it doesn't run out
        crd = card.split(' ')
        specialCard(nextPlayer, card)
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


def specialCard(nextPlayer, card):
    crd = card.split(' ')
    move = crd[1]

    if move == '+4':  # Wild +4
        for i in range(4):
            randCard = random.choice(deck)
            nextPlayer.myCards.append(randCard)  # Adds card to computer's stack
            deck.remove(randCard)  # Removes card from deck
        skippedTurn.append('skip')  # Skips turn
    elif move == '+2':  # Colour +2
        for i in range(2):
            randCard = random.choice(deck)
            nextPlayer.myCards.append(randCard)  # Adds card to computer's stack
            deck.remove(randCard)  # Removes card from deck
        skippedTurn.append('skip')  # Skips turn
    elif move == 'SKIP':  # Colour skip
        skippedTurn.append('skip')
    elif move == 'REVERSE':  # Colour reverse
        reversedTurn.append('reverse')

    # Nothing happens for wild cards; only changes colour


def compPutCardDown(nextPlayer):
    card = random.choice(compPlayCards)
    compPlayCard(nextPlayer, card)
    print(f'[ PLAYED CARD: {card} ]')


def compPlayCard(nextPlayer, card):
    global compPlayedCard

    if card not in specialCards:
        compCards.remove(card)
        deck.append(card)  # Returns card to deck so it doesn't run out
        compPlayedCard = card
    else:  # It's a special card
        compCards.remove(card)
        deck.append(card)  # Returns card to deck so it doesn't run out
        crd = card.split(' ')
        compSpecialCard(nextPlayer, card)
        if crd[0] == 'WILD':
            col = compWildCard()
            card = col + ' CARD'
        compPlayedCard = card


def compWildCard():
    colours = ['RED', 'BLUE', 'YELLOW', 'GREEN']
    choice = random.choice(colours)

    return choice


def compSpecialCard(nextPlayer, card):
    crd = card.split(' ')
    move = crd[1]

    if move == '+4':  # Wild +4
        for i in range(4):
            randCard = random.choice(deck)
            nextPlayer.myCards.append(randCard)  # Adds card to player's stack
            deck.remove(randCard)  # Removes card from deck
        skippedTurn.append('skip')  # Skips turn
    elif move == '+2':  # Colour +2
        for i in range(2):
            randCard = random.choice(deck)
            nextPlayer.myCards.append(randCard)  # Adds card to player's stack
            deck.remove(randCard)  # Removes card from deck
        skippedTurn.append('skip')  # Skips turn
    elif move == 'SKIP':  # Colour skip
        skippedTurn.append('skip')
    elif move == 'REVERSE':  # Colour reverse
        reversedTurn.append('reverse')


def drawCard(user, player, card):
    if user == 'Player':
        randCard = cards.getRandomCard(card, gameplay)
        player.myCards.append(randCard)  # Adds card to your stack
        print(f'[ {player.myName.upper()} DREW A CARD ]')
        skippedTurn.clear()
        reversedTurn.clear()
    elif user == 'Computer':
        randCard = random.choice(deck)
        compCards.append(randCard)  # Adds card to computer's stack
        print('[ THE COMPUTER DREW A CARD ]')
        skippedTurn.clear()
        reversedTurn.clear()

    deck.remove(randCard)  # Removes card from deck


cards = Cards()

playerOne = Player()
playerOne.myName = 'Player 1'

playerTwo = Player()
playerTwo.myName = 'Player 2'

comp = Computer()
comp.myName = 'Computer'

deck = cards.deck
specialCards = cards.specialCards

compCards = comp.myCards

players = []
players.append(playerOne)
players.append(comp)
players.append(playerTwo)

intro()
