'''

    Project by Nora Calif :)

'''

import random
import time
from datetime import datetime

from cards import Cards
from player import Player
from player import Computer

cards = Cards()
games = []
players = []

skippedTurn = []
reversedTurn = []
specialSkip = []


def menu():
    print('\nUNO — PYTHON VER.')
    print('-> made by Nora Calif')

    menuOptions()


def menuOptions():
    print('\nMENU:')
    print('1. New game  \n2. Saved games  \n3. Instructions  \n4. Exit Program')

    # Loop for redirecting based on choice
    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input())
            if choice == 1:
                gaveInput = True
                playerOptions()
            elif choice == 2:
                gaveInput = True
                loadGames()
            elif choice == 3:
                gaveInput = True
                instructions()
            elif choice == 4:
                gaveInput = True
                print('\n----------')
                print('\n-> Have a nice day! \n')
                quit()
            else:
                print('\n-> Choose from the options!')
        except ValueError:
            print('\n-> Enter a valid input!')


def instructions():
    pass


def loadGames():
    print('\n----------')

    if len(games) == 0:  # No game info in the games list
        print('\n[ NO SAVED GAMES ]')
        print('\n----------')
        menuOptions()
    else:  # Games are stored
        print('\nSaved Games:')
        print('(ordered from recent -> oldest)')

        games.reverse()  # Reverses the list so 1st entry is the most recent
        counter = 1
        for i in games:
            print(f'{counter}. {i[0]}')  # Prints the date & time when saved for identification
            counter += 1

        chooseGame(counter)


def chooseGame(counter):
    print('\n[ Which game would you like to resume? ]')

    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input())
            if choice > counter or choice < 1:  # Picked an option not on the list
                print('\n-> Choose from the options!')
            else:
                gaveInput = True
                resumeGame(choice)
        except ValueError:
            print('\n-> Enter a valid input!')


def resumeGame(choice):
    # Resets player list and creates new player objects
    players.clear()
    slots = resetPlayers()

    # Collects data from the game selected & removes from saved list
    gameInfo = games[choice - 1]
    games.remove(games[choice - 1])

    # Separates game info into its components
    playerList = gameInfo[1]
    gameStates = gameInfo[2]
    cardStates = gameInfo[3]

    # Sets current states to the ones from the game
    resumePlayerData(playerList, slots)
    resumeGameData(gameStates)
    resumeCardData(cardStates)

    deckCard = cardStates[0]
    startRound(deckCard)  # Starts game


def resumePlayerData(playerList, slots):
    # Adding back player data
    for i in range(len(playerList)):
        players.append(slots[i])

    for i in range(len(players)):
        attributes = playerList[i]
        players[i].myName = attributes[0]
        players[i].type = attributes[1]
        players[i].myCards = attributes[2]
        players[i].teammate = attributes[3]


def resumeGameData(gameStates):
    # Adding back game data
    cards.gameplay = gameStates[0]

    skippedTurn.clear()
    for i in gameStates[1]:
        skippedTurn.append(i)

    reversedTurn.clear()
    for i in gameStates[2]:
        reversedTurn.append(i)

    specialSkip.clear()
    for i in gameStates[3]:
        specialSkip.append(i)


def resumeCardData(cardStates):
    # Adding back card data
    cards.deck = cardStates[1]
    cards.specialCards = cardStates[2]


def getTime():
    now = datetime.now()  # Gets the current time

    # Splits it into separate elements for date & time
    dateAndTime = str(now).split(' ')

    # Cleans up the time element to include only hours:minutes
    time = dateAndTime[1]
    hrsMinsSecs = time.split('.')
    hrsMinsSecs = hrsMinsSecs[0]  # Gets rid of numbers after the decimal
    hrsMins = hrsMinsSecs.split(':')
    hrsMins = hrsMins[0] + ':' + hrsMins[1]  # Gets rid of seconds

    # Replaces previous time element with shortened one
    dateAndTime.pop()
    dateAndTime.append(hrsMins)

    # Combines date & time into a single string again
    currentTime = dateAndTime[0] + ' ' + dateAndTime[1]

    return currentTime  # Returns current time


def saveGame(lastCard):
    gameInfo = []

    # Saves data from game
    playerList = savePlayerData()
    gameStates = saveGameData()
    cardStates = saveCardData(lastCard)

    # Gets the current date & time
    now = getTime()
    now = now.split(' ')

    # Adds the current time + game data in gameInfo list
    gameInfo.append(f'{now[0]} at {now[1]}')
    gameInfo.append(playerList)
    gameInfo.append(gameStates)
    gameInfo.append(cardStates)

    games.append(gameInfo)  # Adds game info to games list

    print('\n\n--------------------\n')
    menuOptions()  # Sends player back to menu


def savePlayerData():
    playerList = []

    for i in players:
        # Stores info on player attributes
        playerInfo = []

        playerInfo.append(i.myName)
        playerInfo.append(i.type)
        playerInfo.append(i.myCards)
        playerInfo.append(i.teammate)

        playerList.append(playerInfo)  # Adds player info to the players list

    return playerList


def saveGameData():
    gameplayMode = cards.gameplay

    # Creates lists to mimic the skippedTurn, reversedTurn, and specialSkip ones
    skips = []
    for i in skippedTurn:
        skips.append(i)

    reverses = []
    for i in reversedTurn:
        reverses.append(i)

    specials = []
    for i in specialSkip:
        specials.append(i)

    # Stores info on the game states
    gameStates = [gameplayMode, skips, reverses, specials]

    return gameStates


def saveCardData(lastCard):
    if len(specialSkip) <= 1:
        cardOnDeck = lastCard
    else:
        cardOnDeck = str(specialSkip[0])
        counter = 0
        for j in specialSkip:
            if counter != 0:
                cardOnDeck += str(f' / {j}')
            counter += 1
        cardOnDeck += str(' STACKED')

    gameDeck = cards.deck
    gameSpecials = cards.specialCards

    # Stores info on cards
    cardStates = [cardOnDeck, gameDeck, gameSpecials]

    return cardStates


def playerOptions():
    players.clear()
    slots = resetPlayers()

    print('\nMATCH TYPES:')
    print('1. Against the computer  \n2. Against players on same device')

    gaveInput = False
    while not gaveInput:
        try:
            choice = input('')
            choice = int(choice)
            if choice == 1:
                gaveInput = True
                players.append(slots[0])
                players.append(slots[5])
                enterNames()
            elif choice == 2:
                gaveInput = True
                multiOptions(slots)
                break
            else:
                print('\n-> Choose from the options!')
        except ValueError:
            print('\n-> Enter a valid input!')


def multiOptions(slots):
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
                gaveInput = True
                for i in range(choice):
                    players.append(slots[i])
        except ValueError:
            if choice.upper() == 'TM':
                gaveInput = True
                for i in range(4):
                    players.append(slots[i])
                teamMode()
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
    # Resets states
    cards.deck = []
    cards.specialCards = []
    cards.playCards = []
    cards.gameplay = 0

    print('\n[ Which mode of gameplay do you want? ]')

    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input('1. Beginner  2. Easy  3. Normal  \n'))
            if choice == 1:
                gaveInput = True
                cards.gameplay = 3
            elif choice == 2:
                gaveInput = True
                cards.gameplay = 2
            elif choice == 3:
                gaveInput = True
                cards.gameplay = 1
            else:
                print('\n-> Choose from the options!')
        except ValueError:
            print('\n-> Enter a valid input!')

    handCards()


def handCards():
    # Adds cards to cards.deck
    cards.populateCards()
    deck = cards.deck

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

    playableCards(i, lastCard, deckCard)

    if len(playCards) != 0:
        try:
            putCardDown(i, deckCard)
        except IndexError:
            putCardDown(i, deckCard)
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
            players.reverse()  # Reverses order
        # If there are two players, nothing happens (considered to be a skip)
        reversedTurn.clear()
    else:
        players.remove(i)
        players.append(i)

    types = []
    for j in players:
        types.append(j.type)

    # if 'Computer' not in types:
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
        menu()
    else:
        print('\n----------')
        print('\nGame over! Computer won')
        menu()


def checkIfWon():
    playersWon = []
    for i in players:
        if len(i.myCards) == 0:
            playersWon.append(i)

    return playersWon


def playableCards(player, card, deckCrdList):
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
                    stackCard(stackPlayCards, player, deckCard)
                elif len(skippedTurn) != 0:
                    choice = input('\n-> Your turn has been skipped! Press enter to continue')
                    if choice == '':  # Pressed enter
                        gaveInput = True
                        skippedTurn.clear()
                    elif choice.lower() == 'save':
                        gaveInput = True
                        saveGame(deckCrdList)
                else:
                    choice = input('\n-> Press enter to draw a card!')
                    if choice == '':  # Pressed enter
                        gaveInput = True
                        drawCard(player, card)
                    elif choice.lower() == 'save':
                        gaveInput = True
                        saveGame(deckCrdList)
                    # If they don't press enter it just prompts them again
        else:
            drawCard(player, card)


def stackCard(stackPlayCards, player, deckCard):
    global playCards

    print('\n-> Stack a special card on top or pick up?')

    gaveInput = False
    while not gaveInput:
        try:
            choice = input('1. COUNTER ATTACK \n2. PICK UP CARDS  \n')
            choice = int(choice)
            if choice == 1:
                gaveInput = True
                playCards = stackPlayCards
            elif choice == 2:
                pickUpCards(player)
                gaveInput = True
            else:
                print('\n-> Choose from the options!')
        except ValueError:
            if choice.lower() == 'save':
                gaveInput = True
                saveGame(deckCard)
            else:
                print('\n-> Enter a valid input!')


def pickUpCards(player):
    if len(specialSkip) != 0:
        amount = 0

        for i in specialSkip:
            crd = i.split(' ')
            crd = crd[1]
            crd = crd.split('+')
            amnt = crd[1]
            num = int(amnt)
            amount += num

        for i in range(amount):
            randCard = random.choice(cards.deck)
            player.myCards.append(randCard)  # Adds card to computer's stack
            cards.deck.remove(randCard)  # Removes card from cards.deck

        specialSkip.clear()


def putCardDown(player, deckCard):
    global playCards, stackPlayCards

    gaveInput = False
    validCard = False

    if player.type == 'Player':
        if len(stackPlayCards) != 1:
            while not gaveInput:
                try:
                    choice = input('\n-> What card # would you like to play?  \n')
                    if choice.lower() == 'save':
                        gaveInput = True
                        saveGame(deckCard)
                    else:
                        choice = int(choice)
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

    if card not in cards.specialCards:
        player.myCards.remove(card)
        cards.deck.append(card)  # Returns card to cards.deck so it doesn't run out
        playedCard = card
    else:  # It's a special card
        player.myCards.remove(card)
        cards.deck.append(card)  # Returns card to cards.deck so it doesn't run out
        crd = card.split(' ')
        specialCard(card)
        if crd[0] == 'WILD':
            if player.type == 'Player':
                wildCardPrompt()
                card = colour + ' ' + crd[1]
                if len(specialSkip) > 0:
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

    cards.deck.remove(randCard)  # Removes card from cards.deck


def resetPlayers():
    # Creates 5 new player objects with reset states
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

    slots = [playerOne, playerTwo, playerThree, playerFour, playerFive, comp]

    return slots


# Starts at the beginning of the program
menu()
