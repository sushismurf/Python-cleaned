# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 19:36:01 2023.

A horce racing game.

@author: doga
"""
import random


def nameRandomizer(n):
    """
    Create random names for horses.

    Parameters
    ----------
    n : int
        number of horses.

    Returns
    -------
    horseNames : list
        list of horse names without repetition.

    """
    randAdjectiveList = ['Sparkling', 'Serene', 'Flashy', 'Radiant',
                         'Wholesome', 'Elegant', 'Furious', 'Quirky',
                         'Friendly', 'Tired', 'Enigmatic', 'Melancholic',
                         'Luminous', 'Excited', 'Legendary', 'True',
                         'Eerie', 'Cute', 'Anxious', 'Edgy', 'Natural']
    randNounList = ['Sapphire', 'Lettuce', 'Bonsai', 'Chandelier',
                    'Fiddlesticks', 'Kitty', 'Storm', 'Paradox',
                    'Muffin', 'Sands', 'Egg', 'Soup',
                    'Leader', 'Lord', 'Aspargus', 'Observer']
    horseNames = []
    for i in range(n):
        ad1 = random.choice(randAdjectiveList)
        sub1 = random.choice(randNounList)
        if f'{ad1} {sub1}' not in horseNames:
            horseNames.append(f'{ad1} {sub1}')
        else:
            while f'{ad1} {sub1}' in horseNames:
                ad1 = random.choice(randAdjectiveList)
                sub1 = random.choice(randNounList)
            horseNames.append(f'{ad1} {sub1}')
    return horseNames


def roundWinner(p, n):
    """
    Select 3 (or less) horses and make them winners.

    Parameters
    ----------
    p : list
        list of horse names.
    n : int
        to check if horseNum >= 3.

    Returns
    -------
    p1 : str
        winner1.
    p2 : str
        winner2.
    p3 : str
        winner3.
    """
    if n >= 3:
        p1 = random.choice(p)
        p2 = random.choice(p)
        p3 = random.choice(p)
        if p1 == p2 or p1 == p3 or p2 == p3:
            while p1 == p2 or p1 == p3 or p2 == p3:
                p1 = random.choice(p)
                p2 = random.choice(p)
                p3 = random.choice(p)
            return p1, p2, p3
        return p1, p2, p3
    else:
        p1 = random.choice(p)
        p2 = random.choice(p)
        if p1 == p2:
            while p1 == p2:
                p1 = random.choice(p)
                p2 = random.choice(p)
            return p1, p2
        return p1, p2


def daGame(a):
    """
    Game itself but in a function for repetitive uses.

    Returns
    -------
    bal : int
        the amount of money player has won/lost from betting.

    """
    global bal
    print('Welcome to another round of this amazing horse race simulation.')
    playerBet = 0
    horseNum = input('Enter the number of horses you want to see racing: ')
    try:
        horseNum = int(horseNum)
    except ValueError:
        print('It gotta be an integer, ya know...')
    if horseNum <= 0:
        print('Dude.')
    elif horseNum == 1:
        print('I think we got a winner right here...')
    else:
        horseList = []
        for i in range(0, horseNum):
            horseList.append(i)
        for j in range(0, horseNum):
            horseList[j] = nameRandomizer(horseNum)[j]
        roundNum = input('Enter how many rounds you want them to race: ')
        print('')
        try:
            roundNum = int(roundNum)
        except ValueError:
            print('It gotta be an integer, ya know...')
        if roundNum <= 0:
            print('Not sure how that will work buddy.')
        else:
            idk = []
            for k in range(0, roundNum):
                idk.append(roundWinner(horseList, horseNum))
            horseDict = {}
            for u in idk:
                for u1 in u:
                    if u1 not in horseDict.keys():
                        horseDict[u1] = 0
                        if u1 == u[0]:
                            horseDict[u1] += 3
                        elif u1 == u[1]:
                            horseDict[u1] += 2
                        elif u1 == u[2]:
                            horseDict[u1] += 1
                    else:
                        if u1 == u[0]:
                            horseDict[u1] += 3
                        elif u1 == u[1]:
                            horseDict[u1] += 2
                        elif u1 == u[2]:
                            horseDict[u1] += 1
        print('Here are the name of the horses: ')
        for naem in horseList[:-1]:
            print(naem, end=', ')
        print(f'{horseList[-1]}\n')
        better = input('Would you like to play bet? (yes/no): ')
        betVal = None
        if better.strip().lower() == 'yes':
            betGuess = input('Enter the name of the horse you wish to see as '
                             'the winner: ')
            for b in horseList:
                if betGuess.lower().strip() in b.lower().strip():
                    betVal = 0
                    break
            if betVal != 0:
                while betVal != 0:
                    print(f"Couldn't find the horse '{betGuess}'.")
                    betGuess = input('Enter the name of the horse you wish to '
                                     'see as the winner: ')
                    for b in horseList:
                        if betGuess.lower().strip() in b.lower().strip():
                            betVal = 0
                            break
            betVal = input('How much are you willing to wager?: ')
            try:
                betVal = int(betVal)
            except ValueError:
                while betVal.isdigit() is False:
                    print('That is not an integer...')
                    betVal = input('How much are you willing to wager?: ')
        else:
            print('Okay, moving on.\n')
        print('Here is how each round went: \n')
        count = 0
        for num in idk:
            count += 1
            print(f'--Round {count}--')
            for num1 in range(len(num)):
                print(f'{num1+1}. {num[num1]}')
            print(' ')
        bestPt = max(horseDict.values())
        bestHorsey = [k for k, v in horseDict.items() if v == bestPt]
        if len(bestHorsey) == 1:
            print('The horse with the highest points was ' + bestHorsey[0] +
                  f'. They scored {bestPt}.\nGive them a round of applause!')
        else:
            print('Horses with the highest points were ' + str(bestHorsey) +
                  f'. They all scored {bestPt}.\nGive them a round'
                  ' of applause!')
        tempi = []
        for ili in bestHorsey:
            tempi.append(ili.lower().strip())
        if betVal is not None:
            if betGuess.lower().strip() in tempi:
                print(f'You guessed the winner would be {betGuess}, and you'
                      ' were absolutely correct. Congratulations! You won'
                      f' your bet and got {betVal}.')
                bal += betVal
            else:
                if betGuess.lower().strip() not in tempi:
                    print(f'You guessed the winner would be {betGuess}, and'
                          ' you'
                          ' got it wrong...Better luck next time! You lost'
                          f' your bet and have {betVal} less in your '
                          'pockets now.')
                    bal -= betVal
        else:
            playerBet = 0
        print(f'Your current balance: {bal + playerBet}')
        another = input('Up for another round? (yes/no): ')
        if another.lower().strip() == 'yes':
            return playerBet, 'yes'
        else:
            return playerBet, 'no'


print('Welcome to this super great horse race simulation.')
# playerBet = 0
horseNum = input('Enter the number of horses you want to see racing: ')
try:
    horseNum = int(horseNum)
except ValueError:
    print('It gotta be an integer, ya know...')
if horseNum <= 0:
    print('Dude.')
elif horseNum == 1:
    print('I think we got a winner right here...')
else:
    horseList = []
    for i in range(0, horseNum):
        horseList.append(i)
    for j in range(0, horseNum):
        horseList[j] = nameRandomizer(horseNum)[j]
    roundNum = input('Enter how many rounds you want them to race: ')
    print('')
    try:
        roundNum = int(roundNum)
    except ValueError:
        print('It gotta be an integer, ya know...')
    if roundNum <= 0:
        print('Not sure how that will work buddy.')
    else:
        idk = []
        for k in range(0, roundNum):
            idk.append(roundWinner(horseList, horseNum))
        horseDict = {}
        for u in idk:
            for u1 in u:
                if u1 not in horseDict.keys():
                    horseDict[u1] = 0
                    if u1 == u[0]:
                        horseDict[u1] += 3
                    elif u1 == u[1]:
                        horseDict[u1] += 2
                    elif u1 == u[2]:
                        horseDict[u1] += 1
                else:
                    if u1 == u[0]:
                        horseDict[u1] += 3
                    elif u1 == u[1]:
                        horseDict[u1] += 2
                    elif u1 == u[2]:
                        horseDict[u1] += 1
    print('Here are the name of the horses: ')
    for naem in horseList[:-1]:
        print(naem, end=', ')
    print(f'{horseList[-1]}\n')
    better = input('Would you like to play bet? (yes/no): ')
    betVal = None
    if better.strip().lower() == 'yes':
        betGuess = input('Enter the name of the horse you wish to see as '
                         'the winner: ')
        for b in horseList:
            if betGuess.lower().strip() in b.lower().strip():
                betVal = 0
                break
        if betVal != 0:
            while betVal != 0:
                print(f"Couldn't find the horse '{betGuess}'.")
                betGuess = input('Enter the name of the horse you wish to '
                                 'see as the winner: ')
                for b in horseList:
                    if betGuess.lower().strip() in b.lower().strip():
                        betVal = 0
                        break
        betVal = input('How much are you willing to wager?: ')
        try:
            betVal = int(betVal)
        except ValueError:
            while betVal.isdigit() is False:
                print('That is not an integer...')
                betVal = input('How much are you willing to wager?: ')
    else:
        print('Okay, moving on.\n')
    print('Here is how each round went: \n')
    count = 0
    for num in idk:
        count += 1
        print(f'--Round {count}--')
        for num1 in range(len(num)):
            print(f'{num1+1}. {num[num1]}')
        print(' ')
    bestPt = max(horseDict.values())
    bestHorsey = [key for key, value in horseDict.items() if value == bestPt]
    if len(bestHorsey) == 1:
        print('The horse with the highest points was ' + bestHorsey[0] +
              f'. They scored {bestPt}.\nGive them a round of applause!')
    else:
        print('Horses with the highest points were ' + str(bestHorsey) +
              f'. They all scored {bestPt}.\nGive them a round of applause!')
    tempi = []
    for ili in bestHorsey:
        tempi.append(ili.lower().strip())
    if betVal is not None:
        if betGuess.lower().strip() in tempi:
            print(f'You guessed the winner would be {betGuess}, and you'
                  ' were absolutely correct. Congratulations! You won'
                  f' your bet and got {betVal}.')
            playerBet = betVal
        else:
            if betGuess.lower().strip() not in tempi:
                print(f'You guessed the winner would be {betGuess}, and you'
                      ' got it wrong...Better luck next time! You lost'
                      f' your bet and have {betVal} less in your pockets now.')
                playerBet = -betVal
        bal = playerBet
    else:
        playerBet = 0
        bal = playerBet
    print(f'Your current balance: {bal}')
    another = input('Up for another round? (yes/no): ')
    counter = 1
    if another.lower().strip() == 'yes':
        jj = daGame(playerBet)
        counter += 1
        bal += jj[0]
        if jj[1] == 'yes':
            while True:
                jj = daGame(int(jj[0]))
                counter += 1
                bal += jj[0]
                if jj[1] == 'no':
                    break
            print(f'You played {counter} rounds, and finished with {bal}'
                  ' in your pockets.')
            print('Have a nice day!')
        else:
            print('You played 2 rounds, and'
                  f' finished with {bal} in your pockets.')
            print('Have a nice day!')
    else:
        print('You played a single round, and'
              f' finished with {bal} in your pockets.')
        print('Have a nice day!')
