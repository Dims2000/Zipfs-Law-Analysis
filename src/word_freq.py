"""
CSAPX Project 1 Activity 3: Word Frequency

Given a comma separated value file and a word, this program
prints a list of the highest word occurrences (up to and including OUTPUT) and a
loglog graph of the data (-p). This demonstrates Zipf's Law

$ python3 word_freq.py [-h] [-o OUTPUT] [-p] word filename

Author: Dmitry Selin

Date Created: September 21, 2019
Last Modified: September 21, 2019
"""

import matplotlib.pyplot as plt
import util
import argparse
import sys


def word_frequency(word_dict: dict) -> [tuple]:
    """
    Determines the number of occurrences for each word in
    the passed dictionary

    :param word_dict: dictionary where words are keys and their years and usage would be in lists as value
    :return: a list of two element tuples (first element = word, second element = total number of occurrences)

    Pre: word_dict must be a dictionary structured in the way as described above
    Post: None
    """

    # Creates a list with tuples out of word_dict, where the first element in the tuple is a word
    # and the second element is the total number of occurrences for the corresponding word (total_words)
    word_usage_list = [(word, util.total_words(tup)) for (word, tup) in word_dict.items()]

    # Sorts the list based on the values in the second element (usage) in each tuple, and reverses the list
    # (to ensure that the words with the most occurrences appear at the front of the list)
    word_usage_list.sort(key=lambda tup: tup[1])
    word_usage_list.reverse()

    return word_usage_list


def main() -> None:
    """
    Determines and prints the number of occurrences of each word in
    filename in ranked order and prints the results in the console (-o)
    and or as a loglog plot (-p)

    :return: None

    Pre: the file with file name filename must exist and be a csv type file and the command line arguments must be structured correctly
    Post: None
    """

    # Creates a argument parser
    parser = argparse.ArgumentParser()

    # Creates the mandatory command line arguments word and filename
    parser.add_argument("word", help="a word to display the overall ranking of")
    parser.add_argument("filename", help="a comma separated value unigram file")

    # Creates the optional command line arguments output and plot
    parser.add_argument("-o", "--output", type=int, help="display the top OUTPUT (#) ranked words by number of occurrences")
    parser.add_argument("-p", "--plot", help="plot the word rankings from top to bottom based on occurrences", action="store_true")

    # Pareses the command line arguments into args, makes filename, word, and output independent variables,
    # and uses a helper function, read_file, to create a dictionary of words out of file, filename
    args = parser.parse_args()
    filename = args.filename
    output = args.output
    word = args.word
    word_dict = util.read_file(filename)

    # Checks if word appears in word_dict (therefore, in filename), if not,
    # print a standard error and terminate the program
    if word not in word_dict:
        sys.stderr.write("Error: " + args.word + " does not appear!\n")
        exit(2)

    # Sets word_usage_list to a list of tuples, where the first element in the tuple is a word, and the second is the number of occurrences
    word_usage_list = word_frequency(word_dict)

    # Creates a new variable, limit (this variable will determine how many words and their occurrences are printed out by the console)
    limit = output if output is not None and output < len(word_usage_list) else len(word_usage_list)

    # Sets rank_of_word to the index of the tuple word is part of in word_usage_list
    rank_of_word = str(word_usage_list.index((word, util.total_words(word_dict[word]))) + 1)

    # Prints the rank of word
    print(word + " is ranked #" + rank_of_word)

    # Iterates through the elements of word_usage_list and prints the elements from 0 to limit
    for index in range(limit):
        print("#" + str(index + 1) + ": " + word_usage_list[index][0] + " -> " + str(word_usage_list[index][1]))

    # Checks if plot was enabled by the user
    if args.plot:

        # Creates a tuple of numbers from 1 to the length of word_usage_list + 1
        index = range(1, len(word_usage_list) + 1)

        # Creates a loglog plot with the x axis as index, the y axis as a list of every second element in every tuple in word_usage_list,
        # a green colored line, and a linewidth of 0.75 (default was 1)
        plt.loglog(index, [usage for word, usage in word_usage_list], color="green", linewidth=0.75)

        # Creates x and y axis labels, the graph title, and sets the margins of the graph to 0
        plt.xlabel('Rank of word ("' + word + '" is ranked ' + rank_of_word + ')'), plt.ylabel("Total number of occurrences")
        plt.title("Word Frequencies: " + filename.split("/")[1])
        plt.margins(0)

        # Creates a dots for every point in the graph with size 10 and a blue color
        plt.scatter(index[1:-1], [usage for word, usage in word_usage_list[1:-1]], s=10, color="blue")

        # Creates a marker and label for the user-chosen word in the graph (red star)
        plt.scatter(int(rank_of_word), util.total_words(word_dict[word]), color="red", s=110, marker="*", zorder=7, edgecolors="black")
        plt.text(int(rank_of_word) + float(0.04 * float(rank_of_word)), util.total_words(word_dict[word]) +
                 float(0.09 * float(util.total_words(word_dict[word]))), word, fontsize=9)

        # Sets the ticks of the graph to face inwards and appear on the top and right of the graph
        plt.tick_params(axis="both", direction="in", top=True, right=True, width=0.5)

        # Displays the plot
        plt.show()


if __name__ == '__main__':
    main()
