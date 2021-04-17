import random


class Cards:

    def __init__(self):
        self.deck = []
        self.specialCards = []
        self.playCards = []
        self.stackPlayCards = []
        self.gameplay = 0

    def populateCards(self):
        """Populates the deck with cards and adds the special ones in a separate list"""
        moves = ['+2', 'SKIP', 'REVERSE']
        colours = ['RED', 'YELLOW', 'GREEN', 'BLUE']
        wildMoves = ['+4', 'CARD']

        for num in range(10):  # Adds numbers 0-9 to the moves list
            moves.append(f'{num}')

        for num in range(2):  # Ensures each card gets added twice
            for i in colours:
                for j in moves:  # Creates a card w/ each move & colour combination
                    self.deck.append(f'{i} {j}')

            for i in wildMoves:  # Creates the two variations of wild cards
                self.deck.append(f'WILD {i}')
                self.deck.append(f'WILD {i}')

        self.specialCardCheck()

    def specialCardCheck(self):
        """Checks for special cards in the deck"""
        for i in self.deck:  # Goes through each card in the deck
            move = str(i).split(' ')

            try:
                testIfInt = int(str(move[1]))  # Raises an exception for most special cards
                if move[1] == '+2' or move[1] == '+4':  # To account for +2 and +4 cards
                    self.specialCards.append(i)
            except ValueError:  # Move isn't a number (ex. 'REVERSE' or 'SKIP')
                self.specialCards.append(i)

    def playableCards(self, cards, deckCard):
        """Checks for playable cards based on the card on top of the deck"""
        self.playCards.clear()

        for i in cards:
            # Checks if card is playable
            card = str(i).split(' ')
            if card[0] == deckCard[0]:  # Colour matches
                self.playCards.append(i)
            elif card[1] == deckCard[1]:  # Move matches
                self.playCards.append(i)
            elif card[0] == 'WILD':  # Since wild cards are always playable
                self.playCards.append(i)

    def stackPlayableCards(self, cards, deckCard):
        """Checks for stackable cards if there's a +2 or +4 on the deck"""
        self.stackPlayCards.clear()

        for i in cards:
            specialType = i.split(' ')
            specialType = specialType[1]

            if specialType == '+4':
                self.stackPlayCards.append(i)

            if deckCard[1] == '+2':  # +2 cards can only be stacked on top of another +2
                if specialType == '+2':
                    self.stackPlayCards.append(i)

    def getRandomCard(self, cardOnDeck):
        """Returns a random card from the deck, or often a matching one if in beginner mode"""
        if self.gameplay != 3:  # Normal or Easy mode
            drawnCard = random.choice(self.deck)
        else:  # Beginner mode
            matchingCards = self.checkForMatching(cardOnDeck)
            # To create a 70% chance of drawing a matching card
            chance = random.randint(0, 10)
            if chance < 7:
                drawnCard = random.choice(matchingCards)
            else:
                drawnCard = random.choice(self.deck)

        return drawnCard

    def checkForMatching(self, cardOnDeck):
        """Returns cards that matches the one on top of the deck"""
        card = str(cardOnDeck).split(' ')
        matchingCards = []

        for i in self.deck:
            deckCrd = i.split(' ')
            if card[0] == deckCrd[0]:  # Colour is the same
                matchingCards.append(i)
            elif card[1] == deckCrd[1]:  # Move is the same
                matchingCards.append(i)

        return matchingCards
