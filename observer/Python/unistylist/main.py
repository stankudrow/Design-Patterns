#!/usr/bin/env python3
"""
A demonstration of subjects/observers.

Inspiration from the book "Software Design Patterns" by Sufyan bin Uzayr.
"""


from observers import Paragraph
from subjects import FontStylist


if __name__ == "__main__":
    stylist = FontStylist()  # greetings from a concrete one
    par1 = Paragraph('P1')
    par2 = Paragraph('P2')
    # registration
    stylist.register(par2)
    print(f"{par2.name} has been registered as an observer.")
    # before
    for par in par1, par2:
        print(par)
    stylist.style = {
        'colour': 'green',
        'size': '16pt',
        'font': 'Comic Sans',
    }
    print("I have unified them all!")
    # after
    for par in par1, par2:
        print(par)
