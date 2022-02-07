import time
from bank import Bank
import datetime
from datetime import datetime as dt
bank = Bank()



# -------------------------


def overview():
    payWeek = bank.payWeek()

    print("\n----------")
    print("\nBanking Report for Narura Calif")

    print("\n| THIS WEEK")
    print(f"You spent: ${float(bank.getSpending()):.2f}")
    print(f"You earned: ${float(bank.getEarnings()):.2f}")

    if float(bank.getSpending()) >= float(bank.getEarnings()):
        if not payWeek:
            print("-> It's okay, spending is typically larger than earnings if it's not a pay week.")
        else:
            print("-> Take some time to reflect! This is ridiculous spending.")
    else:
        print("\n-> Great job saving, Narura!")

    print("\n| BALANCE")
    print(f"Chequing: ${float(bank.getChequing()):.2f}")
    print(f"Savings: ${float(bank.getSavings()):.2f}")

    pcGoal = 2000
    pcProgress = (float(bank.getSavings()) / pcGoal)*100
    print(f"\n-> You are {pcProgress:.0f}% through your goal of getting a PC!")
    if payWeek:
        if float(bank.getChequing()) > 50:
            print("-> You might wanna cut down on the amount of spending money you allocate, though.")
        elif float(bank.getChequing()) < 15:
            print("-> You might wanna be more generous with the spending money, though")
        else:
            print("Enjoy your spending money for the week :D")
    if not payWeek:
        if float(bank.getChequing()) < 7:
            print("-> Sheesh! You need to relax with the spending.")
        else:
            print("Enjoy your spending money for the week :D")


# -------------------------


def addOrSubtract(which):
    print("\n----------")
    amount = float(input("\nAmount: "))
    account = input("Chequing or savings: ")

    if which == "add":
        bank.addToWeekEarning(amount)
    elif which == "subtract":
        essential = input("\nIs this essential? \n")
        if essential == "no":
            bank.addToWeekSpending(amount)
        else:
            pass
        amount = 0 - amount

    bank.addSubtractMoney(account, amount)
    menu()

def transfer():
    print("\n----------")
    amount = float(input("\nAmount: "))
    account = input("Recipient account: ")

    if account == "chequing":
        bank.addSubtractMoney(account, amount)
        bank.addSubtractMoney("savings", 0 - amount)
    elif account == "savings":
        bank.addSubtractMoney(account, amount)
        bank.addSubtractMoney("chequing", 0 - amount)

    menu()

def transaction():
    improperChoice = True
    print("\n----------")
    print("\n| OPTIONS \n")
    print("1. Add money to account")
    print("2. Subtract money from account")
    print("3. Transfer money between accounts \n")

    while improperChoice:
        try:
            choice = float(input("ACCESS #: "))
            if choice == 1:
                improperChoice = False
                addOrSubtract("add")
            elif choice == 2:
                improperChoice = False
                addOrSubtract("subtract")
            elif choice == 3:
                improperChoice = False
                transfer()
            else:
                pass
        except ValueError:
            pass


# -------------------------


def advising():
    payWeek = bank.payWeek()
    balance = float(bank.getChequing())

    print("\n----------")
    cost = float(input("\nCost: "))

    if balance - cost < 0:
        print("\n-> No way! You don't even have enough money.")
    elif balance - cost == 0:
        print("\n-> You know that's a dumb purchase. Don't consider it.")
    else:
        if payWeek:
            if balance - cost <= 10:
                print("\n-> Since you're getting paid soon, I suppose...")
            else:
                print("\n-> As long as you're happy with the purchase, go ahead!")
        else:
            if balance - cost <= 5:
                print("\n-> No. Full stop. Narura, you will regret this later.")
            elif balance - cost <= 12:
                assured = input("\nWill you regret this in 3 hours: ")
                if assured == "no":
                    print("\n-> Then I guess you should go ahead")
                if assured == "yes":
                    print("\n-> Then don't disappoint yourself and SAVE YOUR MONEY!")
            else:
                print("\n-> As long as you're happy with the purchase, go ahead!")

    time.sleep(3)
    menu()


# -------------------------


def menu():
    improperChoice = True
    print("\n\n--------------------")
    print("   BUDGETING APP")
    print("  coded by Nora")
    print("--------------------\n")

    print("\n| SERVICES \n")

    weekday = dt.today().weekday()

    if weekday == 5 or weekday == 6:
        print("1. Weekly overview")
        print("2. Record transaction")
        print("3. Financial advising\n")
    else:
        print("1. Record transaction")
        print("2. Financial advising\n")

    while improperChoice:
        try:
            uChoice = input("ACCESS #: ")
            choice = float(uChoice)
            if weekday == 5 or weekday == 6:
                if choice == 1:
                    improperChoice = False
                    overview()
                elif choice == 2:
                    improperChoice = False
                    transaction()
                elif choice == 3:
                    improperChoice = False
                    advising()
                else:
                    pass
            else:
                if choice == 1:
                    improperChoice = False
                    transaction()
                elif choice == 2:
                    improperChoice = False
                    advising()
                else:
                    pass
        except ValueError:
            if uChoice == "end":
                quit()
            else:
                pass

menu()