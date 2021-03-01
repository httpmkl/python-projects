class BankAccount:

    def __init__(self, initialDeposit, password = None):
        # The initial deposit was converted to a float in the Store file before getting sent here
        self.balance = initialDeposit

        if password is None:
            print('\n[ Please enter a password for your account ]')
            self.setPassword()

    def setPassword(self):
        global password
        password = input('Password: ')
        confirmPassword = input('Confirm password: ')
        if password != confirmPassword:
            print('\nSorry, password doesn\'t match! \n')
            self.setPassword()
        else:
            print('\n-> Password set! Your account is now ready for use')

    def getPassword(self):
        return password

    # Returns true if you have more balance than cost, false if you don't
    def canAfford(self, amount):
        if(float(amount) <= self.balance):
            return True
        else:
            return False

    def makePurchase(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'{amount} spent from your account.')
            print(f'You now have ${self.balance} remaining.')
        else:
            print('You do not have enough funds left to afford this item.')

    def balanceReport(self):
        print(f'You have $ {self.balance} left in your account.')
