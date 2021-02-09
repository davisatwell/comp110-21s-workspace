"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730384155"



how_much: int = int(input("Pick a number between 1-100: "))

if how_much < 100:
        print("You will get an A on your next test.")
else: 
    if how_much < 75:
        print("You will fall in love soon")
if how_much < 50:
    print("Someone really misses you.")
if how_much < 25:
        print ("You will try a new food soon.")
