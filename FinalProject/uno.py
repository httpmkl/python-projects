'''

    Project by Nora Calif :)

'''

import random
import time
from datetime import datetime

from cards import Cards
from players import Player
from players import Computer

cards = Cards()
games = []
players = []

skippedTurn = []
reversedTurn = []
specialSkip = []


def menu():
    print('\nUNO — PYTHON VER.')
    print('-> made by Nora Calif')

    skippedTurn.clear()
    reversedTurn.clear()
    specialSkip.clear()

    menuOptions()


def menuOptions():
    print('\nMENU:')
    print('1. New game  \n2. Saved games  \n3. Exit Program')

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
                print('\n--------------------')
                print('\n-> Have a nice day! \n')
                quit()
            else:
                print('\n-> Choose from the options!')
        except ValueError:
            print('\n-> Enter a valid input!')


def loadGames():
    print('\n----------')

    if len(games) == 0:  # No game info in the games list
        print('\n[ NO SAVED GAMES ]')
        print('\n----------')
        menuOptions()
    else:  # Games are saved
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
        cardOnDeck = lastCard  # Grabs the last card on deck
    else:  # If cards are being stacked
        cardOnDeck = str(specialSkip[0])
        counter = 0
        for i in specialSkip:
            if counter != 0:
                cardOnDeck += str(f' / {i}')
            counter += 1
        cardOnDeck += str(' STACKED')

    # Collects current deck and special cards
    gameDeck = cards.deck
    gameSpecials = cards.specialCards

    # Stores info on the card states
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
            if choice == 1:  # Match against computer
                gaveInput = True
                # Adds player 1 & computer
                players.append(slots[0])
                players.append(slots[5])
                enterNames()
            elif choice == 2:  # Match against others on the same device
                gaveInput = True
                multiOptions(slots)
            else:
                print('\n-> Choose from the options!')
        except ValueError:
            print('\n-> Enter a valid input!')


def multiOptions(slots):
    print('\n[ How many players? Enter a value from 2-5, or type \'TM\' for Team Mode ]')
    print('-> Team Mode is only available for 4 players!')

    gaveInput = False
    while not gaveInput:
        try:
            choice = input()

            if choice.upper() == 'TM':  # Chose team mode
                gaveInput = True
                for i in range(4):
                    # Appends 4 players to list
                    players.append(slots[i])
                teamMode()  # Puts them in teams

            else:  # Didn't choose team mode
                choice = int(choice)
                if choice < 2 or choice > 5:  # Chose a value below 2 or above 5
                    print('\n-> Only 2-5 players for multiplayer!')
                else:  # Chose a valid amount
                    gaveInput = True
                    for i in range(choice):
                        # Appends the amount of players selected
                        players.append(slots[i])

        except ValueError:
            print('\n-> Enter a valid amount!')

    enterNames()  # Redirects to choose names


def teamMode():
    # Adds the two teams
    teamOne = addTeamOne()
    teamTwo = addTeamTwo()

    # Appends players back into list so they alternate teams
    players.append(teamOne[0])
    players.append(teamTwo[0])
    players.append(teamOne[1])
    players.append(teamTwo[1])


def addTeamOne():
    teamOne = []

    # Picks 2 random player and removes from players list
    onePl1 = random.choice(players)
    players.remove(onePl1)
    teamOne.append(onePl1)
    onePl1.myName = 'Player 1'

    onePl2 = random.choice(players)
    players.remove(onePl2)
    teamOne.append(onePl2)
    onePl2.myName = 'Player 3'

    # Sets their teammate to each other
    onePl1.teammate = onePl2
    onePl2.teammate = onePl1

    return teamOne


def addTeamTwo():
    teamTwo = []

    # Picks 2 random player and removes from players list
    twoPl1 = random.choice(players)
    players.remove(twoPl1)
    teamTwo.append(twoPl1)
    twoPl1.myName = 'Player 2'

    twoPl2 = random.choice(players)
    players.remove(twoPl2)
    teamTwo.append(twoPl2)
    twoPl2.myName = 'Player 4'

    # Sets their teammate to each other
    twoPl1.teammate = twoPl2
    twoPl2.teammate = twoPl1

    return teamTwo


def enterNames():
    for i in players:
        if i.type == 'Player':
            print(f'\n-> Enter the name for {i.myName}')

            # Sets player name to input
            name = input()
            i.myName = name

    gameplayPrompt()


def gameplayPrompt():
    # Resets card states
    cards.deck = []
    cards.specialCards = []
    cards.playCards = []
    cards.gameplay = 0

    print('\n[ Which mode of gameplay do you want? ]')

    # Loop for selecting gameplay
    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input('1. Beginner  2. Easy  3. Normal  \n'))
            if choice == 1:  # Beginner
                gaveInput = True
                cards.gameplay = 3
            elif choice == 2:  # Easy
                gaveInput = True
                cards.gameplay = 2
            elif choice == 3:  # Normal
                gaveInput = True
                cards.gameplay = 1
            else:
                print('\n-> Choose from the options!')
        except ValueError:
            print('\n-> Enter a valid input!')

    handCards()


def handCards():
    # Adds cards to deck
    cards.populateCards()
    deck = cards.deck

    for i in players:
        for num in range(7):
            # Chooses 7 random cards for player
            randCard = random.choice(deck)
            i.myCards.append(randCard)  # Adds card to stack
            deck.remove(randCard)  # Removes card from deck

    deckCard = [random.choice(deck)]  # Picks a random card to start
    startRound(deckCard)


def startRound(deckCard):
    i = players[0]  # Gets the first player in the list

    controlTurn(i, deckCard)
    additionalTurnStuff(i)

    startRound(deckCard)  # Loops back up


def controlTurn(i, deckCard):
    print('\n----------')

    # Prints last card on deck (or multiple if stacked)
    lastCard = deckCard[len(deckCard) - 1]
    if len(specialSkip) <= 1:
        print(f'\nCard on deck: {lastCard}')
    else:
        # Prints in "CARD / CARD / ... STACKED" format
        lastCards = str(specialSkip[0])
        counter = 0
        for j in specialSkip:
            if counter != 0:
                lastCards += str(f' / {j}')
            counter += 1

        print(f'\nCard on deck: {lastCards} STACKED')

    # Does turn for player & computer
    if i.type == 'Player':
        doTurn(i, lastCard, deckCard)
    else:
        if len(skippedTurn) == 0 and len(specialSkip) == 0:
            doTurn(i, lastCard, deckCard)
        else:  # Their turn has been skipped or a special card has been placed
            compSkip(i, lastCard, deckCard)


def compSkip(player, lastCard, deckCrdList):
    deckCard = str(lastCard).split(' ')

    if len(specialSkip) != 0:
        # Checks for +4 or +2 cards to stack
        cards.stackPlayableCards(player.myCards, deckCard)

        if len(cards.stackPlayCards) == 0:
            skippedTurn.append('skip')  # Becomes a skip if no stackable cards
        else:
            # Playable cards are now the stackable ones
            cards.playCards.clear()
            for i in cards.stackPlayCards:
                cards.playCards.append(i)

            # Proceeds with turn as usual
            putCardDown(player, deckCrdList)

    if len(skippedTurn) != 0:
        pickUpCards(player)  # Picks up cards if necessary
        print('THEIR TURN HAS BEEN SKIPPED!')
        skippedTurn.clear()


def doTurn(i, lastCard, deckCard):
    # Gathers and prints playable cards
    playableCards(i, lastCard, deckCard)

    if len(cards.playCards) != 0:  # If they have playable cards
        putCardDown(i, deckCard)


def additionalTurnStuff(i):
    # Check for if game is over
    playersWon = checkIfWon()
    if len(playersWon) > 0:
        gameOver(playersWon[0])

    # Reverses order if card was placed
    if len(reversedTurn) != 0:
        if len(players) > 2:
            players.reverse()  # Reverses order
        # If there are two players, nothing happens (considered to be a skip)
        reversedTurn.clear()
    else: # Goes to the next player if no reverse
        players.remove(i)
        players.append(i)

    # Adds buffer (for games with multiple players)
    types = []
    for j in players:
        types.append(j.type)

    if 'Computer' not in types:
        buffer(players[0])


def buffer(i):
    print('\n----------')

    # Prints a long column of lines
    for num in range(20):
        print('|')

    print(f'FOUR SECONDS BEFORE {i.myName.upper()}\'s CARDS SHOW...')
    print('-> switch over the device and don\'t peak!')

    for num in range(20):
        print('|')

    time.sleep(4)  # Waits 4 seconds before continuing


def gameOver(player):
    print('\n\n--------------------')

    if player.teammate is not None:  # If on team mode
        print(f'\nGAME OVER: {player.myName} and {player.teammate.myName} won')
    else:  # If it's a normal game
        print(f'\nGAME OVER: {player.myName} won')

    print('\n--------------------\n')
    menu()  # Redirects back to menu


def checkIfWon():
    playersWon = []

    for i in players:
        if len(i.myCards) == 0:
            playersWon.append(i)

    return playersWon  # Returns players with no cards (typically, it'll be just one)


def playableCards(player, card, deckCrdList):
    deckCard = str(card).split(' ')  # Splits card on deck into its colour & number/type
    cards.playableCards(player.myCards, deckCard)  # Checks for playable cards

    if player.type == 'Player':
        if player.teammate is not None:
            # Prints teammates cards if they have one
            print(f'\nYOUR TEAMMATE: {player.teammate.myName}')
            counter = 1
            for i in player.teammate.myCards:
                print(f'{counter}. {i}')
                counter += 1

        if len(specialSkip) != 0:
            # Checks for stackable cards if there's a +4 or +2 on top of the deck
            cards.stackPlayableCards(player.myCards, deckCard)

            if len(cards.stackPlayCards) == 0:
                # Turn becomes a skip if no stackable cards are present
                skippedTurn.append('skip')

        printCards(player)  # Prints cards

    proceedWithTurn(player, card, deckCrdList, deckCard)


def printCards(player):
    counter = 1
    print(f'\n{player.myName} Cards:')

    for i in player.myCards:
        # Prints cards
        if len(cards.stackPlayCards) == 0:
            pickUpCards(player)  # Picks up cards if necessary
            if i in cards.playCards and cards.gameplay != 1:
                print(f'{counter}. [ {i} ]')
            else:
                print(f'{counter}. {i}')
        else:  # Only highlights stackable cards if a +4/+2 is on deck
            if i in cards.stackPlayCards and cards.gameplay != 1:
                print(f'{counter}. [ {i} ]')
            else:
                print(f'{counter}. {i}')

        counter += 1  # Updates counter

        if len(skippedTurn) != 0 or len(specialSkip) != 0:
            # Clears playable cards if a skip or special skip is done
            cards.playCards.clear()


def proceedWithTurn(player, card, deckCrdList, deckCard):
    if len(cards.playCards) == 0:  # No playable cards
        if player.type == 'Player':
            # Loop for accepting valid input
            gaveInput = False
            while not gaveInput:

                # If turn was skipped
                if len(skippedTurn) != 0:
                    choice = input('\n-> Your turn has been skipped! Press enter to continue')
                    if choice == '':  # Pressed enter
                        gaveInput = True
                        skippedTurn.clear()
                    elif choice.lower() == 'save':
                        gaveInput = True
                        saveGame(deckCrdList)

                # If there's a special skip
                elif len(specialSkip) != 0:
                    gaveInput = True
                    stackCard(player, deckCard)

                # If they just have no playable cards
                else:
                    choice = input('\n-> Press enter to draw a card!')
                    if choice == '':  # Pressed enter
                        gaveInput = True
                        drawCard(player, card)
                    elif choice.lower() == 'save':
                        gaveInput = True
                        saveGame(deckCrdList)

        else:  # Computer automatically draws a card
            drawCard(player, card)


def stackCard(player, deckCard):
    print('\n-> Stack a special card on top or pick up?')

    # Loop for accepting valid input
    gaveInput = False
    while not gaveInput:
        try:
            choice = input('1. COUNTER ATTACK \n2. PICK UP CARDS  \n')

            # Exits game if typed save
            if choice.lower() == 'save':
                gaveInput = True
                saveGame(deckCard)
            else:
                choice = int(choice)

                if choice == 1:  # Chose counter attack
                    gaveInput = True
                    # Stackable cards becomes playable cards
                    cards.playCards.clear()
                    for i in cards.stackPlayCards:
                        cards.playCards.append(i)
                elif choice == 2:  # Chose to pick up cards
                    pickUpCards(player)
                    gaveInput = True
                else:  # Chose an option not stated
                    print('\n-> Choose from the options!')

        except ValueError:
            print('\n-> Enter a valid input!')


def pickUpCards(player):
    if len(specialSkip) != 0:
        amount = 0

        for i in specialSkip:
            # Splits up the card name to retrieve the amount that has to be added to deck
            crd = str(i).split(' ')
            crd = crd[1]
            crd = crd.split('+')
            amnt = crd[1]
            num = int(amnt)
            amount += num  # Adds it to the total amount (in case of multiple special cards)

        for i in range(amount):
            randCard = random.choice(cards.deck)
            player.myCards.append(randCard)  # Adds cards to player's stack
            cards.deck.remove(randCard)  # Removes card from deck

        specialSkip.clear()


def checkForValidity(card):
    validCard = False

    # Checks if card is present in the playable cards list
    for i in cards.playCards:
        if card == i:
            validCard = True  # Chosen card is playable

    return validCard


def putCardDown(player, deckCard):
    gaveInput = False

    if player.type == 'Player':
        if len(cards.stackPlayCards) != 1:  # If they have multiple stackable cards
            # Loop for accepting valid input
            while not gaveInput:
                try:
                    choice = input('\n-> What card # would you like to play?  \n')
                    if choice.lower() == 'save':  # Chose to save
                        gaveInput = True
                        saveGame(deckCard)
                    else:
                        choice = int(choice)
                        if 0 < choice <= len(player.myCards):  # If card is within range on their stack
                            card = player.myCards[choice - 1]
                            validCard = checkForValidity(card)  # Checks if the card is playable
                            if validCard:  # Choose a valid card
                                gaveInput = True
                            else:  # Didn't choose a valid card
                                print('[ This is not a playable card! ]')
                        else:
                            print('\n-> Enter a valid input!')
                except ValueError:
                    print('\n-> Enter a valid input!')
        else:  # If they have one stackable card, it's automatically picked
            card = cards.stackPlayCards[0]
    else:  # Computer picks a random card amongst their playable ones
        card = random.choice(cards.playCards)

    playedCard = playCard(player, card)
    deckCard.append(playedCard)
    print(f'[ PLAYED CARD: {card} ]')


def playCard(player, card):
    player.myCards.remove(card)
    cards.deck.append(card)  # Returns card to the deck so it doesn't run

    if card in cards.specialCards:  # It's a special card
        # Split's card title to get its attributes
        crd = card.split(' ')
        specialCard(card)

        if crd[0] == 'WILD':  # Wild card or wild +4
            if player.type == 'Player':
                col = wildCardPrompt()  # Asks for which colour to change into
            elif player.type == 'Computer':
                col = compWildCard() # Picks a random colour

            card = col + ' ' + crd[1]  # Changes 'wild' to selected colour

            # Updates 'WILD +4' entry in the specialSkip lists if necessary
            if len(specialSkip) > 0:
                if specialSkip[len(specialSkip) - 1] == 'WILD +4':
                    specialSkip.pop()
                    specialSkip.append(card)

    playedCard = card
    return playedCard


def wildCardPrompt():
    print('\n[ Which colour do you want to set the card to? ]')

    # Loop for accepting valid input
    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input('1. Red | 2. Blue | 3. Yellow | 4. Green  \n'))
            # Sets colour based on choice
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

    return colour


def specialCard(card):
    crd = card.split(' ')
    move = crd[1]

    # Appends move/card into the designated list
    if move == '+4':  # Wild +4
        specialSkip.append(card)
    elif move == '+2':  # Colour +2
        specialSkip.append(card)
    elif move == 'SKIP':  # Colour skip
        skippedTurn.append('skip')
    elif move == 'REVERSE':  # Colour reverse
        reversedTurn.append('reverse')


def compWildCard():
    # Chooses a random entry from the list of colours are returns
    colours = ['RED', 'BLUE', 'YELLOW', 'GREEN']
    choice = random.choice(colours)

    return choice


def drawCard(player, cardOnDeck):
    randCard = cards.getRandomCard(cardOnDeck)  # Gets a random card
    player.myCards.append(randCard)  # Adds card to stack
    cards.deck.remove(randCard)  # Removes card from deck
    print(f'[ {player.myName.upper()} DREW A CARD ]')

    skippedTurn.clear()
    reversedTurn.clear()


def resetPlayers():
    # Creates 5 new player objects and enters it into the slots list
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
