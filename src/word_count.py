"""
CSAPX Project 1 Activity 1: Word Count

Given a comma separated value file, Word Count finds
the number of occurrences of a user-specified word throughout the file

$ python3 word_count.py word filename

Author: Dmitry Selin

Date Created: September 16, 2019
Last Modified: September 20, 2019
"""

import argparse
import sys


def main():
    """

    :return: None
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("words", help="a word to display the total occurrences of")
    parser.add_argument("filename", help="a comma separated value unigram file")

    args = parser.parse_args()
    word = args.words
    file = ""

    try:
        file = open("../" + args.filename)

    except FileNotFoundError:
        sys.stderr.write("Error: " + args.filename + " does not exist!\n")
        exit(1)

    word_count = 0

    for line in file:
        components = line.strip().split(',')

        if components[0] == word:
            word_count += int(components[2])

    if word_count == 0:
        sys.stderr.write("Error: " + word + " does not appear!\n")
        exit(1)

    print(word + ": " + str(word_count))


if __name__ == '__main__':
    main()
