"""
CSAPX Project: Helper Functions

A module with snippets of code that are used multiple
times throughout Project 1

Author: Dmitry Selin

Date Created: September 19, 2019
Last Modified: September 21, 2019
"""

import collections
import sys
from typing import List


def read_file(filename: str) -> dict:
    """
    Reads a file (filename) and parses the lines of the .csv file
    into a dictionary

    :param filename: a string with the the name of a csv file in the form data/name-of-file
    :return: a dictionary with words as keys and lists with tuples of years and occurrences as elements

    Pre: the file with the name filename must exist be formatted as a csv file type
    Post: the returned dictionary will contain one or more elements of listings as values for each key
    """

    # Initializes file as a blank string
    file = ""

    # Attempts to open the user-given file, if the file is not found, an exception is
    # thrown, a standard error is displayed, and the program is terminated
    try:
        file = open("../" + filename)

    except FileNotFoundError:
        sys.stderr.write("Error: " + filename + " does not exist!\n")
        exit(1)

    # Initializes Usage (for better readability) and occurrences (the dictionary that will be returned)
    Usage = collections.namedtuple("Usage", ("year", "occurrence"))
    occurrences = {}

    # Iterates through each line in file
    for line in file:

        # Splits line into its 3 components (parses by commas) and strips any excess whitespace
        components = line.strip().split(',')

        # Creates a Usage tuple, entry, with the 2 components as parameters
        # components[0] = word, components[1] = year, components[2] = number of occurrences
        entry = Usage(components[1].strip(), components[2].strip())
        word = components[0].strip().lower()

        # If the word is already a key, append its year and usage to its value list as a tuple,
        # otherwise, simply add a new entry to occurrences
        if word in occurrences:
            occurrences[word].append(entry)
        else:
            occurrences[word] = [entry]

    return occurrences


def total_words(target_word: List) -> int:
    """
    Adds the number of occurrences a particular word has and returns the number

    :param target_word: a list of two-element tuples that contain the year and number of occurrences of a particular word
    :return: int (word_count)

    Pre: target_word must contain two-element tuples, where the second element in each tuple is the usage of the word
    Post: None
    """

    # Initializes word_count
    word_count = 0

    # Iterates through each listing of a word occurrence in target_word and adds the second element
    # (the word usage) to word_count
    for listing in target_word:
        word_count += int(listing.occurrence)

    return word_count
