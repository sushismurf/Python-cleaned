"""Checks whether the word is a palindrome or not."""

word = input('Input the word you wish to be checked: ').strip()
word_reverse = word[::-1]
is_word = True

for letter in word:
    if not letter.isalpha():
        is_word = False
        print('Please provide a word.')
        break

if letter.isalpha():
    if word_reverse == word:
        print('The word is a palindrome.')
    else:
        print('The word is not a palindrome.')
