'''

    What I added:
        - All of the basic UNO gameplay mechanics
        - The ability to play against the computer
        - UN0's special cards (Wild (card & +4), +2, reverse, skip)
            - The computer's ability to use special cards
        - Different modes of gameplay (beginner/easy/normal)
        - Multiplayer options
        - Improved reverse mechanics
        - Menu screen to contain & organize these features
        - Generalize player functions to adapt to computer plays
        - Team mode for even numbers (in multiplayer)
        - The ability to stack special cards to avoid picking up
            - The prevention of stacking +2 on top of a +4

    What I need to add/do:
        - The ability to reverse wild cards
        - Unique special cards (that are not in UNO)
        - Save/load game abilities
        - Ensure everything is modular & organized before submitting

'''

import random
import time
from cards import Cards
from player import Player
from player import Computer

myCards = []

skippedTurn = []
reversedTurn = []
specialSkip = []


def menu():
    print('\nUNO — PYTHON VER.')
    print('-> made by Nora Calif')

    print('\nMENU:')
    print('1. New game  \n2. Saved games  \n3. Instructions')

    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input())
            if choice == 1:
                playerOptions()
                gaveInput = True
            elif choice == 2:
                print('\nUnder Construction')
                gaveInput = True
            elif choice == 3:
                print('\nUnder Construction')
                gaveInput = True
            else:
                print('\n-> Choose from the options!')
        except ValueError:
            print('\n-> Enter a valid input!')

def playerOptions():
    print('\nMATCH TYPES:')
    print('1. Against the computer  \n2. Against players on same device')

    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input())
            if choice == 1:
                players.append(playerOne)
                players.append(comp)
                enterNames()
                gaveInput = True
            elif choice == 2:
                multiOptions()
                gaveInput = True
            else:
                print('\n-> Choose from the options!')
        except ValueError:
            print('\n-> Enter a valid amount!')

def multiOptions():
    print('\n[ How many players? Enter a value from 2-5, or TM for Team Mode ]')
    print('-> Team Mode is only available for 4 players!')

    gaveInput = False
    while not gaveInput:
        try:
            choice = input()
            choice = int(choice)
            if choice < 2 or choice > 5:
                print('\n-> Only 2-5 players for multiplayer!')
            else:
                for i in range(choice):
                    players.append(slots[i])
                gaveInput = True
        except ValueError:
            if choice.upper() == 'TM':
                for i in range(4):
                    players.append(slots[i])
                teamMode()
                gaveInput = True
            else:
                print('\n-> Enter a valid amount!')

    enterNames()

def teamMode():
    teamOne = []

    onePl1 = random.choice(players)
    players.remove(onePl1)
    teamOne.append(onePl1)
    onePl1.myName = 'Player 1'

    onePl2 = random.choice(players)
    players.remove(onePl2)
    teamOne.append(onePl2)
    onePl2.myName = 'Player 3'

    onePl1.teammate = onePl2
    onePl2.teammate = onePl1

    teamTwo = []

    twoPl1 = random.choice(players)
    players.remove(twoPl1)
    teamTwo.append(twoPl1)
    twoPl1.myName = 'Player 2'

    twoPl2 = random.choice(players)
    players.remove(twoPl2)
    teamTwo.append(twoPl2)
    twoPl2.myName = 'Player 4'

    twoPl1.teammate = twoPl2
    twoPl2.teammate = twoPl1

    players.append(onePl1)
    players.append(twoPl1)
    players.append(onePl2)
    players.append(twoPl2)

def enterNames():
    for i in players:
        if i.type == 'Player':
            print(f'\n-> Enter the name for {i.myName}')

            name = input()
            i.myName = name

    gameplayPrompt()

def gameplayPrompt():
    print('\n[ Which mode of gameplay do you want? ]')

    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input('1. Beginner  2. Easy  3. Normal  \n'))
            if choice == 1:
                cards.gameplay = 3
                gaveInput = True
            elif choice == 2:
                cards.gameplay = 2
                gaveInput = True
            elif choice == 3:
                cards.gameplay = 1
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

def turn(i, lastCard, deckCard):
    for num in range(len(players)):
        if i == players[num]:
            nextPlayer = num + 1

    playableCards(i, lastCard, players[nextPlayer])

    if len(playCards) != 0:
        try:
            putCardDown(i)
        except IndexError:
            putCardDown(i)
        deckCard.append(playedCard)

def startRound(deckCard):
    global playCards, stackPlayCards

    i = players[0]  # First player in the list

    print('\n----------')

    lastCard = deckCard[len(deckCard) - 1]
    if len(specialSkip) <= 1:
        print(f'\nCard on deck: {lastCard}')
    else:
        lastCards = str(specialSkip[0])
        counter = 0
        for j in specialSkip:
            if counter != 0:
                lastCards += str(f' / {j}')
            counter += 1

        print(f'\nCard on deck: {lastCards} STACKED')

    if i.type == 'Player':
        turn(i, lastCard, deckCard)
    else:
        if len(skippedTurn) == 0:
            turn(i, lastCard, deckCard)
        elif len(skippedTurn) != 0:  # Their turn has been skipped
            print('THEIR TURN HAS BEEN SKIPPED!')
            skippedTurn.clear()

    playCards.clear()
    stackPlayCards.clear()

    playersWon = checkIfWon()
    if len(playersWon) > 0:
        gameOver(playersWon[0])

    if i == players[len(players) - 1]:  # Last player
        startRound(deckCard)

    if len(reversedTurn) != 0:
        if len(players) > 2:
            players.reverse()   # Reverses order
        # If there are two players, nothing happens (considered to be a skip)
        reversedTurn.clear()
    else:
        players.remove(i)
        players.append(i)

    types = []
    for j in players:
        types.append(j.type)

    #if 'Computer' not in types:
    #    buffer(players[0])

    startRound(deckCard)  # Loops back up

def buffer(i):
    print('\n----------')

    for num in range(20):
        print('|')

    print(f'FOUR SECONDS BEFORE {i.myName.upper()}\'s CARDS SHOW...')
    print('-> switch over the device and don\'t peak!')

    for num in range(20):
        print('|')

    time.sleep(4)

def gameOver(player):
    if player.type == 'Player':
        print('\n----------')
        if player.teammate is not None:
            print(f'\nGame over! {player.myName} and {player.teammate.myName} won')
        else:
            print(f'\nGame over! {player.myName} won')
        quit()
    else:
        print('\n----------')
        print('\nGame over! Computer won')
        quit()

def checkIfWon():
    playersWon = []
    for i in players:
        if len(i.myCards) == 0:
            playersWon.append(i)

    return playersWon


def playableCards(player, card, nextPlayer):
    global playCards, stackPlayCards

    deckCard = str(card).split(' ')
    cards.playableCards(player.myCards, deckCard)
    playCards = cards.playCards
    stackPlayCards = []

    if player.type == 'Player':
        if player.teammate is not None:
            print(f'\nYOUR TEAMMATE: {player.teammate.myName}')
            counter = 1
            for i in player.teammate.myCards:
                print(f'{counter}. {i}')
                counter += 1

        counter = 1
        print(f'\n{player.myName} Cards:')

        if len(specialSkip) != 0:
            for i in player.myCards:
                specialType = i.split(' ')
                specialType = specialType[1]

                if specialType == '+4':
                    stackPlayCards.append(i)

                if deckCard[1] == '+2':  # Only on a +2 you can stack a +2
                    if specialType == '+2':
                        stackPlayCards.append(i)

            if len(stackPlayCards) == 0:
                skippedTurn.append('skip')

        for i in player.myCards:
            # Prints card
            if len(stackPlayCards) == 0:
                pickUpCards(player)
                if i in playCards and cards.gameplay != 1:
                    print(f'{counter}. [ {i} ]')
                else:
                    print(f'{counter}. {i}')
            else:
                if i in stackPlayCards and cards.gameplay != 1:
                    print(f'{counter}. [ {i} ]')
                else:
                    print(f'{counter}. {i}')

            counter += 1  # Updates counter

        if len(skippedTurn) != 0 or len(specialSkip) != 0:
            playCards.clear()

    if len(playCards) == 0:  # No playable cards
        if player.type == 'Player':
            gaveInput = False
            while not gaveInput:
                if len(specialSkip) != 0:
                    gaveInput = True
                    stackCard(stackPlayCards, player)
                elif len(skippedTurn) != 0:
                    choice = input('\n-> Your turn has been skipped! Press enter to continue')
                    if choice == '':  # Pressed enter
                        gaveInput = True
                        skippedTurn.clear()
                else:
                    choice = input('\n-> Press enter to draw a card!')
                    if choice == '':  # Pressed enter
                        gaveInput = True
                        drawCard(player, card)
                    # If they don't press enter it just prompts them again
        else:
            drawCard(player, card)

def stackCard(stackPlayCards, player):
    global playCards

    print('\n-> Stack a special card on top or pick up?')

    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input('1. COUNTER ATTACK \n2. PICK UP CARDS  \n'))
            if choice == 1:
                gaveInput = True
                playCards = stackPlayCards
            elif choice == 2:
                pickUpCards(player)
                gaveInput = True
            else:
                print('\n-> Choose from the options!')
        except ValueError:
            print('\n-> Enter a valid input!')

def pickUpCards(player):
    if len(specialSkip) != 0:
        amount = 0

        for i in specialSkip:
            crd = i.split(' ')
            crd = crd[1]
            amnt = crd.split('+')
            amnt = crd[1]
            num = int(amnt)
            amount += num

        for i in range(amount):
            randCard = random.choice(deck)
            player.myCards.append(randCard)  # Adds card to computer's stack
            deck.remove(randCard)  # Removes card from deck

        specialSkip.clear()

def putCardDown(player):
    global playCards, stackPlayCards

    gaveInput = False
    validCard = False

    if player.type == 'Player':
        if len(stackPlayCards) != 1:
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
                            gaveInput = True
                    else:
                        print('\n-> Enter a valid input!')
                except ValueError:
                    print('\n-> Enter a valid input!')
        else:
            card = stackPlayCards[0]
    else:
        card = random.choice(playCards)

    playCard(player, card)
    print(f'[ PLAYED CARD: {card} ]')


def playCard(player, card):
    global playedCard

    if card not in specialCards:
        player.myCards.remove(card)
        deck.append(card)  # Returns card to deck so it doesn't run out
        playedCard = card
    else:  # It's a special card
        player.myCards.remove(card)
        deck.append(card)  # Returns card to deck so it doesn't run out
        crd = card.split(' ')
        specialCard(card)
        if crd[0] == 'WILD':
            if player.type == 'Player':
                wildCardPrompt()
                card = colour + ' ' + crd[1]
                if specialSkip[len(specialSkip) - 1] == 'WILD +4':
                    specialSkip.pop()
                    specialSkip.append(card)
            elif player.type == 'Computer':
                col = compWildCard()
                card = col + ' CARD'
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
        specialSkip.append(card)  # Skips turn
    elif move == '+2':  # Colour +2
        specialSkip.append(card)  # Skips turn
    elif move == 'SKIP':  # Colour skip
        skippedTurn.append('skip')
    elif move == 'REVERSE':  # Colour reverse
        reversedTurn.append('reverse')
    # Nothing happens for wild cards; only changes colour

def compWildCard():
    colours = ['RED', 'BLUE', 'YELLOW', 'GREEN']
    choice = random.choice(colours)

    return choice

def drawCard(player, card):
    randCard = cards.getRandomCard(card)
    player.myCards.append(randCard)  # Adds card to stack
    print(f'[ {player.myName.upper()} DREW A CARD ]')
    skippedTurn.clear()
    reversedTurn.clear()

    deck.remove(randCard)  # Removes card from deck


cards = Cards()

playerOne = Player()
playerOne.myName = 'Player 1'

playerTwo = Player()
playerTwo.myName = 'Player 2'

playerThree = Player()
playerThree.myName = 'Player 3'

playerFour = Player()
playerFour.myName = 'Player 4'

playerFive = Player()
playerFive.myName = 'Player 5'

comp = Computer()
comp.myName = 'Computer'

deck = cards.deck
specialCards = cards.specialCards

slots = [playerOne, playerTwo, playerThree, playerFour, playerFive]

players = []
menu()
