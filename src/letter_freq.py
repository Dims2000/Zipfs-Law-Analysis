"""

"""

import argparse
import helper_functions
import word_count
import matplotlib.pyplot as plt
import numpy


def letter_frequency(word_dict: dict) -> dict:

    word_list = word_dict.keys()
    num_of_letters = 0

    letters = {"a": 0.0, "b": 0.0, "c": 0.0, "d": 0.0, "e": 0.0, "f": 0.0, "g": 0.0, "h": 0.0, "i": 0.0, "j": 0.0, "k": 0.0, "l": 0.0, "m": 0.0,
               "n": 0.0, "o": 0.0, "p": 0.0, "q": 0.0, "r": 0.0, "s": 0.0, "t": 0.0, "u": 0.0, "v": 0.0, "w": 0.0, "x": 0.0, "y": 0.0, "z": 0.0}

    for word in word_list:
        num_of_words = int(word_count.total_words(word_dict[word]))
        num_of_letters += len(word) * num_of_words

        for letter in range(len(word)):
            letters[word[letter]] += num_of_words

    for key in letters.keys():
        letters[key] = letters[key] / num_of_letters

    return letters


def main():
    """

    :return:
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--output", "-o", help="display letter frequencies to standard output", action="store_true")
    parser.add_argument("filename", help="a comma separated value unigram file")
    parser.add_argument("--plot", "-p", help="plot letter frequencies using matplotlib", action="store_true")

    args = parser.parse_args()
    word_dict = helper_functions.read_file(args.filename)

    if args.plot or args.output:

        letter_frequencies = letter_frequency(word_dict)

        for key in letter_frequencies.keys():
            print(key + ": " + str(letter_frequencies[key]))

        if args.plot:
            index = numpy.arange(len(letter_frequencies.keys()))
            plt.bar(index, letter_frequencies.values(), color="blue", edgecolor="black", linewidth=1, width=1)
            plt.xlabel("Letter")
            plt.ylabel("Frequency")
            plt.title("Letter Frequencies: " + args.filename)
            plt.xticks(index, letter_frequencies.keys())
            plt.margins(0)
            plt.show()


if __name__ == '__main__':
    main()
