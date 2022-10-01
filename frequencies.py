"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    #makes all items in the list a string
    items = [str(i) for i in items]

    while len(items) > 0:
        for i in items:
            value = items.count(i);
            frequencies.update({i : value})

            while items.count(i) > 0:
                items.remove(i)

    return frequencies
