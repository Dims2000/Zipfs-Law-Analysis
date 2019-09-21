"""
CSAPX Project 1 Activity 1: Word Count

Given a comma separated value file, Word Count finds
the number of occurrences of a user-specified word throughout the file

$ python3 word_count.py [-h] word filename

Author: Dmitry Selin

Date Created: September 16, 2019
Last Modified: September 20, 2019
"""

import argparse
import sys
import helper_functions


def main():
    """
    Parses a given .csv file and returns the number of time a
    user-given word appears in the file

    :return: None

    Pre: filename must be be a valid file in the syntax data/filename
    Post: None
    """

    # Creates an argument parser
    parser = argparse.ArgumentParser()

    # Creates two arguments to be taken from the command line
    parser.add_argument("words", help="a word to display the total occurrences of")
    parser.add_argument("filename", help="a comma separated value unigram file")

    # Parses the arguments into args and sets word as its own variable
    args = parser.parse_args()
    word = args.words

    # Utilizes a helper function that reads a file and returns a dictionary with words
    # as keys and a list of tuples that contain the year and usage as internal variables
    words_dict = helper_functions.read_file(args.filename)

    # Uses a helper function that takes a List as a parameter (in this case, the value of
    # the user-given word) and returns its total number of occurrences (aka its usage)
    word_count = helper_functions.total_words(words_dict[word])

    # If a particular word does not exist in the file, a standard error message is displayed and the program is terminated
    if word_count == 0:
        sys.stderr.write("Error: " + word + " does not appear!\n")
        exit(2)

    print(word + ": " + str(word_count))


if __name__ == '__main__':
    main()
