import random


class Cards:

    def __init__(self):
        self.deck = []
        self.specialCards = []
        self.playCards = []

    def populateCards(self):
        moves = ['+2', 'SKIP', 'REVERSE']  # Coloured card moves
        colours = ['RED', 'YELLOW', 'GREEN', 'BLUE']  # Cards colours
        wildMoves = ['+4', 'CARD']  # Wild card moves

        for num in range(10):  # Adds numbers 0-9 to the moves list
            moves.append(f'{num}')

        for num in range(2):  # So each card gets added twice
            for i in colours:
                for j in moves:  # Creates a card w/ each move & colour combination
                    self.deck.append(f'{i} {j}')

            for i in wildMoves:  # Creates the two variations of wild cards
                self.deck.append(f'WILD {i}')
                self.deck.append(f'WILD {i}')

        self.specialCardCheck()

    def specialCardCheck(self):
        for i in self.deck:  # Goes through each card in the deck
            move = str(i).split(' ')  # Splits card name
            try:
                testIfInt = int(str(move[1]))
                if move[1] == '+2' or move[1] == '+4':  # To account for +2 and +4
                    self.specialCards.append(i)
            except ValueError:  # Second word isn't a number (ex. 'REVERSE')
                self.specialCards.append(i)

    def playableCards(self, cards, deckCard):
        for i in cards:
            # Checks if card is playable
            card = str(i).split(' ')
            if card[0] == deckCard[0]:
                self.playCards.append(i)
            elif card[1] == deckCard[1]:
                self.playCards.append(i)
            elif card[0] == 'WILD':
                self.playCards.append(i)

    def getRandomCard(self, card, gameplay):
        if gameplay != 3:  # Normal or Easy mode
            drawnCard = random.choice(self.deck)
        else:  # Beginner2
            matching = self.checkForMatching(card)
            chance = random.randint(0, 10)
            if chance < 7:
                drawnCard = random.choice(matching)
            else:
                drawnCard = random.choice(self.deck)

        return drawnCard

    def checkForMatching(self, card):
        card = str(card).split(' ')
        matchingCards = []

        for i in range(len(self.deck)):
            deckCrd = str(self.deck[i]).split(' ')
            if card[0] == deckCrd[0]:
                matchingCards.append(str(self.deck[i]))
            elif card[1] == deckCrd[1]:
                matchingCards.append(str(self.deck[i]))
            else:
                pass

        return matchingCards
