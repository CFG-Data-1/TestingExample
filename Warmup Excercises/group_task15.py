"""
CFG Graduation Photo Challenge -- SOLUTION

Please watch the demo video, which explains how to approach and solve
this challenge.

This is one of the multiple possible solutions (there might be many others)

This one is:
O(nlogn) time | O(1) space - where n is the number of students
"""


def is_possible_photo(purple, black):
    """
    Calculate whether we can take guidelines compliant photo.
    :param purple: list of ints - students in purple hats heights
    :param black: list of ints - students in black hats heights
    :return: boolean
    """
    purple.sort(reverse=True)
    black.sort(reverse=True)

    first_row_colour = "PURPLE" if purple[0] < black[0] else "BLACK"
    for idx in range(len(purple)):
        purple_height = purple[idx]
        black_height = black[idx]

        if first_row_colour == 'PURPLE':
            if purple_height >= black_height:
                return False
        else:
            if black_height >= purple_height:
                return False
    
    return True
