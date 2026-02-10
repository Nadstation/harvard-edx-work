#docs.python.org/3/library/random.html
#random.choice(seq)

# import random
##from random import choice

#coin = random.choice(["heads","tails"])
##coin = choice(["heads","tails"])

#print(coin)

#random.randint(a, b)
#if you read the documentation, it's a random int that's between A and B inclusive.
#so if you were to pass in 1 for A and 10 for B, you would get back a number between 1 and 10 inclusive, including the 1 and the 10 potentially each with 10% probability.

#import random

#number = random.randint(1,10)
#print(number)

import random
#shuffle(x),
#if you read the documentation for shuffle in the same random module, you will see that it takes in a list, for instance, of values, and just shuffles them up
#it randomizes them like a deck of cards.
#if you read the documentation for random.shuffle, you will see that it shuffles the argument in place. It doesn't return you a value that contains the shuffle cards in this case.
#it actually shuffles the list it's given itself.

cards = ["jack","queen","king"]
random.shuffle(cards)

#print(cards)

for card in cards:
    print(card)










