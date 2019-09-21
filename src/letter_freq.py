"""
CSAPX Project 1 Activity 2: Letter Frequency

Given a comma separated value file, this program
prints a list of floating-point values (-o) and a
bar graph plot (-p) corresponding to the
frequency of letters in the file

$ python3 letter_freq.py [-h] [-o] [-p] filename

Author: Dmitry Selin

Date Created: September 20, 2019
Last Modified: September 21, 2019
"""

import argparse
import util
import matplotlib.pyplot as plt
import numpy


def letter_frequency(word_dict: dict) -> dict:
    """
    Given a dictionary with words and their occurrences,
    this function breaks down how often each letter is used

    :param word_dict: a parsed csv file that has words as keys and a list of two element tuples (year and usage)
    :return: a 26 entry dictionary with all lowercase letter as keys and their rates of appearance as values

    Pre: word_dict must be a valid dictionary as described above
    Post: the returned dictionary will always have 26 entries with float values as values
    """

    # Creates a separate tuple with all the different words in word_dict
    word_list = word_dict.keys()

    # Initializes num_of_letters (total number of all the letters)
    num_of_letters = 0

    # Creates a dictionary with letters a through z as keys and 0.0 for each value
    letters = {chr(letter): 0.0 for letter in range(ord('a'), ord('z') + 1)}

    # Iterates through every word in word_list, calls a helper function to determine the number of occurrences
    # for each word, and adds that number multiplied by the number of letters in word to num_of_letters
    for word in word_list:
        num_of_words = int(util.total_words(word_dict[word]))
        num_of_letters += len(word) * num_of_words

        # Iterates through every every letter in word by iterating through its number index and adds
        # num_of_words (all occurrences of word) to each corresponding letter in letters
        for letter in range(len(word)):
            letters[word[letter]] += num_of_words

    # Iterates through all the keys in letters and divides the number of occurrences of each
    # letter by num_of_letters (total number of letters) to determine the rate of use for each letter
    for key in letters.keys():
        letters[key] = letters[key] / num_of_letters

    return letters


def main() -> None:
    """
    Given a csv filename through the command line, this function
    returns the rates of use for every letter of all the words in the file

    :return: None

    Pre: filename must point to a file that exists and is formatted as a csv file
    Post: None
    """

    # Creates an argument parser
    parser = argparse.ArgumentParser()

    # Creates two optional boolean command line arguments
    parser.add_argument("--output", "-o", help="display letter frequencies to standard output", action="store_true")
    parser.add_argument("--plot", "-p", help="plot letter frequencies using matplotlib", action="store_true")

    # Creates a mandatory command line argument
    parser.add_argument("filename", help="a comma separated value unigram file")

    # Parses the arguments into args and creates a dictionary of filename using the helper function, read_file
    args = parser.parse_args()
    word_dict = util.read_file(args.filename)

    # Checks if the user has requested a plot or a console output of the data, otherwise do nothing
    if args.plot or args.output:

        # Sets letter_frequencies to the dict returned by letter_frequency
        letter_frequencies = letter_frequency(word_dict)

        # Checks if the user requested for a console output of the data
        if args.output:

            # Iterates through all entries in letter_frequencies and prints each word and its rate of usage
            for key in letter_frequencies.keys():
                print(key + ": " + str(letter_frequencies[key]))

        # Checks if the user requested for a bar graph
        if args.plot:

            # Creates a sorted number representation of the keys of letter_frequencies
            index = numpy.arange(len(letter_frequencies.keys()))

            # Creates a bar graph with index as the x axis, values of letter_frequencies (rates) as the y axis,
            # a clue color with a black edge, with a width of 1, no x axis margins, and a slight y axis margin
            plt.bar(index, letter_frequencies.values(), color="blue", edgecolor="black", linewidth=1, width=1)
            plt.margins(0, 0.05)

            # Sets the x and y axis labels and the title
            plt.xlabel("Letter"), plt.ylabel("Frequency")
            plt.title("Letter Frequencies: " + args.filename)

            # Creates ticks for the x axis for each letter (key) in letter_frequencies,
            # includes ticks for the top and right of the graph, and displays the graph
            plt.xticks(index, letter_frequencies.keys())
            plt.tick_params(direction="in", top=True, right=True)
            plt.show()


if __name__ == '__main__':
    main()
