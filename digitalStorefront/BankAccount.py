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
            print('\n-> Sorry, password doesn\'t match! \n')
            self.setPassword()
        else:
            print('\n-> Password set! Your account is now ready for use')

    def getPassword(self):
        return password

    # Returns true if you have more balance than cost, false if you don't
    def canAfford(self, amount):
        if float(amount) <= self.balance:
            return True
        else:
            return False

    def makePurchase(self, amount):
        # NOTE: Removed the conditional logic for checking if user can afford it
        # Affordability was already checked through the function above before accessing this
        self.balance -= amount
        print(f'\n{amount} spent from your account.')
        print(f'You now have ${self.balance:.2f} remaining.')

    def balanceReport(self):
        print(f'You have $ {self.balance:.2f} left in your account.')

    # NOTE: Created for the purpose of refunds (after user returns an item)
    def addMoney(self, num):
        self.balance += num
