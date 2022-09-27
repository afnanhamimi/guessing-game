#!/usr/bin/env python

import random

def main():
    """Start guessing elements and numbers of periodic table game."""
    print("Guess the elements and numbers!")

    periodic = [
        "carbon",
        "silver",
        "antimony",
        "zinc",
        "mercury",
        "lead",
        "silicon",
        "actinum",
        "copper",
        "cerium",
        ]

    x = random.choice(periodic)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What elements am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
        elif x =="carbon":
            print("this elements have a symbolic name as a C and atomic number is 6")
        elif x =="silver":
            print("this elements have a symbolic name as a Ag and atomic number is 47")
        elif x =="antimony":
            print("this elements have a symbolic name as a Sb and atomic number is 51")
        elif x =="zinc":
            print("this elements have a symbolic name as a Zn and atomic number is 30")
        elif x =="mercury":
            print("this elements have a symbolic name as a Hg and atomic number is 80")
        elif x =="lead":
            print("this elements have a symbolic name as a Pb and atomic number is 82")
        elif x =="silicon":
            print("this elements have a symbolic name as a Si and atomic number is 14")
        elif x =="actinum":
            print("this elements have a symbolic name as a Ac and atomic number is 89")
        elif x =="copper":
            print("this elements have a symbolic name as a Cu and atomic number is 29")
        elif x =="cerium":
            print("this elements have a symbolic name as a Ce and atomic number is 58")



main()

