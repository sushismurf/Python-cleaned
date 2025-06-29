"""Assignment 3.

Finds the sum of the first & last digit of a 4-digit number.

"""

numberC = 4387  # 4-digit number (integer)
digit1 = numberC // 1000
digit4 = numberC % 10
sum14 = digit1 + digit4

if numberC >= 1000 and numberC <= 9999 and isinstance(numberC, int):
    print(f'The sum of the first and last digit of the number {numberC} \
is {sum14}.')

if numberC > 9999 or numberC < 1000:
    print('That number is not 4-digits. Please provide a 4-digit number.')

if not isinstance(numberC, int):
    print('That number is not an integer. Please privide an integer.')
