
class Father:

    def __init__(self, age):
        # print('Father created')
        self.age = age
        self.favIntro = 'Hello neighbour!'
        # Initialization is never inherited by child classes (unless super())


    def sayFavPhrase(self):
        print(self.favIntro)

    def sayJoke(self):
        print('Why is 6 afraid of 7? Because 7 8 9')


class Son(Father): # Setting parent class

    def __init__(self, age):
        # Makes it so that the Father's initialization is inherited
        super().__init__(age) # Puts age in brackets so they don't inherit that value

        print('Son created')
        self.age = age
        self.favIntro = 'uh, hey, sup' # Overrides the favourite intro from Father class
        self.favPokemon = 'Charizard' # Son gets this but not dad

    def sayJoke(self): # Overrides Father sayJoke()
        print('Ask me if I\'m a tree.')


father = Father(50)
son = Son(15)

son.favPokemon
son.sayJoke()