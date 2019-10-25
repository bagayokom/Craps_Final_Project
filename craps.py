import random

# Mohamed Bagayoko
# October 24 2019
# Craps! Game


def bankroll():
    error = True
    error2 = True
    while error:
        print("Hello! Welcome to Craps! Please enter your bankroll:")
        create = int(input("> "))
        if create <= 0:
            print("Your input is invalid. Please try again.")
            error = True
        else:
            error = False
    if create > 0:
        print(f"Your bankroll is ${create}")
    print("How much are you betting:")
    while error2:
        bet = int(input("> "))
        if bet > create:
            print("Your bet is greater than your bankroll. Please try again.")
            error2 = True
        else:
            print(f"Your bet is ${bet}")
            error2 = False


def rule_input():
    print("""Do you want me to explain the rules? 
(Enter 1 for Yes/ 2 for No)""")
    rules = input("> ")
    if rules == "1":
        print("""The rules are simple. You get two dice ranging between one and six. 
        The results will be added together. If your result is a 7 or 11, you win! 
        If your dice add up to a 2, 3, or 12, you lose. If neither, your number result is 
        the goal in order to win. You will keep re rolling until you get that number. 
        If you get a 7 however, you lose the game entirely and is asked to use a new bet.""")
        print("Lets get the game started then!")
        print("Enter anything to continue")
        input("> ")
    elif rules == "2":
        print("Lets get the game started then!")


def roll():
    first_dice = 0
    second_dice = 0
    both_dice = 0
    keep_going = True
    while keep_going:
        first_dice = random.randint(1, 6)
        print(f"Your first dice rolled a: {first_dice}")
        print(f"Enter anything to continue")
        input("> ")
        second_dice = random.randint(1, 6)
        print(f"Your second dice rolled a: {second_dice}")
        both_dice = first_dice + second_dice
        point = both_dice
        print(f"Your dice total is a: {both_dice}!")
        if both_dice == 2 or both_dice == 3 or both_dice == 12:
            print("You lose!")
            keep_going = False
        elif both_dice == 7 or both_dice == 11:
            print("You win!")
            keep_going = False
        else:
            while keep_going:
                print(f"Your set point is {point}.")
                print("Enter anything to continue")
                input("> ")
                first_dice = random.randint(1, 6)
                print(f"You rolled a {first_dice}")
                print("Enter anything to continue")
                input("> ")
                second_dice = random.randint(1, 6)
                print(f"You rolled a {second_dice}")
                both_dice = first_dice + second_dice
                print(f"You total is a {both_dice}")
                if both_dice == 7:
                    print("You lose!")
                    keep_going = False
                    print(decision_maker())
                if both_dice == point:
                    print("You win!")
                    keep_going = False
                    print(decision_maker())
                if both_dice != point:
                    print(decision_maker())
                    keep_going = True


def decision_maker():
    decision = int(input())
    print("""Do you want to keep going?
(Enter 1 for Yes/ 2 for No""")
    if decision == 1:
        bankroll()
        if decision == 2:
            print("Have a good day then!")
            keep_going = False


bankroll()
rule_input()
roll()

