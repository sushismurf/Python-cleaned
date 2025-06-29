"""
A clothing store has a sale where if you buy 2
suits you will get a 50% discount on the second.
The 50% discount will be applied to the lowerpriced suit.
If the total purchase cost is over 1000TL, an additional 10%
discount will be applied. Write a program that inputs thecost of
2 suits, and outputs the total purchase cost.
"""

suit1 = float(input('Enter the cosst of the first suit: '))
suit2 = float(input('Enter the cosst of the second suit: '))
totalPrice = suit1 + suit2

if suit1 < 0 or suit2 < 0:
    print('Price must be positive.')

if totalPrice < 1000:
    if suit1 >= suit2:
        print('The total amount you have to pay is', suit1 + suit2 / 2, 'TL.')
    else:
        print('The total amount you have to pay is', suit2 + suit1 / 2, 'TL.')

if totalPrice >= 1000:
    if suit1 >= suit2:
        print('The total amount you have to \
pay is', (suit1 + suit2 / 2) * 0.9, 'TL.')
    else:
        print('The total amount you have to \
pay is', (suit2 + suit1 / 2) * 0.9, 'TL.')
