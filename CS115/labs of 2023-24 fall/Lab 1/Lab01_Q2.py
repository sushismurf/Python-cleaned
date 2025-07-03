#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 15:59:38 2023

"""

card = input("Enter the card notation: ");
      
# extract the value which may be 1 or 2 characters long
value = card[:-1];

# the suit is always the last character
suit = card[-1]

valueAsString = ""
if value == "A":
    valueAsString = "Ace"
elif value == "J":
    valueAsString = "Jack"
elif value == "Q":
    valueAsString = "Queen";
elif value == "K":
    valueAsString = "King";
else:
     valueAsString = value;      
 
suitAsString = "";
if suit == "D":
    suitAsString = "Diamonds"
elif suit == "H":
    suitAsString = "Hearts"
elif suit == "S":
    suitAsString = "Spades"
else:
    suitAsString = "Clubs";
      
print(f'{valueAsString} of {suitAsString}');