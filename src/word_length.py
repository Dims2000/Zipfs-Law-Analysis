"""
CSAPX Project 1 Activity 4: Word Length

Given a comma separated value file and a starting and ending years, this
program prints a list of floating-point values (-o) and a bar graph
plot (-p) corresponding to the average word length for each year in the file

$ python3 word_length.py [-h] [-o] [-p] start end filename

Author: Dmitry Selin

Date Created: September 21, 2019
Last Modified: September 22, 2019
"""

import argparse
import matplotlib.pyplot as plt
import numpy
import util
import sys


def averages(word_dict: dict, start: int, end: int) -> dict:
    """
    Calculates the average word length for each year in between (and including start and end) in word_dict
    and returns a dictionary with years ask keys and averages as values

    :param word_dict: a dictionary with words as keys and a list of namedtuples (Usage) as values
    :param start: an int for the starting year
    :param end: an int for the ending year
    :return: a dictionary with years as keys and average word lengths as values

    Pre: end must be greater than start and word_dict must be on the syntax described above
    Post: the returned dict will have end-start entries
    """

    # Creates a blank dictionary with all the years between and including start and end as keys
    # The value is a tuple with three types: 2 ints and a float
    average_word_len = {str(year): (0, 0, 0.0) for year in range(start, end + 1)}

    # Iterates through all the items in word_dict
    for (word, entry) in word_dict.items():

        # Iterates through all namedtuples in entry (element 1 = year, element 2 = occurrences/usage)
        for (year, usage) in entry:

            # If the year in entry is in between start and end, then run the following script
            if start <= int(year) <= end:

                # word_weight = existing num in the second element of the value of year in average_word_len
                # plus, the length of word multiplied by the usage (used in calculating the average)
                word_weight = average_word_len[year][0] + (len(word) * int(usage))

                # num_of_words = existing num in the first element of the value corresponding to year in average_word_len
                # plus, the usage
                num_of_words = average_word_len[year][1] + int(usage)

                # Updates the values for year in average_word_len (the final element is the current word average for year)
                average_word_len[year] = (word_weight, num_of_words, (word_weight / num_of_words))

    # Creates a dictionary from average_word_len using only the last element if each value as the only value for each year
    word_averages = {key: average_word_len[key][2] for key in average_word_len.keys()}

    return word_averages


def main() -> None:
    """
    Prints a list of word averages between years start and end (-o)
    and a plot of the data (-p)

    :return: None

    Pre: the file with the file name filename must exist and by formatted as a csv
    Post: None
    """

    # Creates an argument parser
    parser = argparse.ArgumentParser()

    # Creates 2 optional arguments: output and plot
    parser.add_argument("-o", "--output", help="display the average word lengths over years", action="store_true")
    parser.add_argument("-p", "--plot", help="plot the average word lengths over years", action="store_true")

    # Creates 3 mandatory arguments: start, end, and filename
    parser.add_argument("start", help="the starting year range")
    parser.add_argument("end", help="the ending year range")
    parser.add_argument("filename", help="a comma separated value unigram file")

    # Parses the command line arguments and sets filename, start, and end as independent variables
    args = parser.parse_args()
    filename = str(args.filename)
    start = int(args.start)
    end = int(args.end)

    # If start is greater than end, then prints a standard error and terminate the program
    if start > end:
        sys.stderr.write("Error: start year must be less than or equal to end year!\n")
        exit(3)

    if args.output or args.plot:

        # Uses a helper function to print a dictionary of the file's contents
        word_dict = util.read_file(filename)

        # Uses the averages function to determine the average word length for each year from start to and including end
        word_averages = averages(word_dict, start, end)

        # if the user requested for console output, print the data from word_averages
        if args.output:
            for key in word_averages:
                print(key + ": " + str(word_averages[key]))

        # If a plot was requested, then run the following script
        if args.plot:

            # Creates a list of numbers from 0 to the length of word_averages
            index = range(len(word_averages))

            # Creates plot with index as the x axis and the corresponding values in word_averages as the y axis
            plt.plot(index, word_averages.values(), color="blue", linewidth=0.75)

            # Sets the x and y labels, as well as the title for the graph
            plt.xlabel("Year"), plt.ylabel("Average word length")
            plt.title("Average word lengths from " + str(start) + " to " + str(end) + ": " + filename.split("/")[1])

            # tick_step and extra_tick are numbers that help to correctly format the ticks in the x axis
            tick_step = len(word_averages) // 7 if len(word_averages) > 7 else 1
            extra_tick = tick_step % 7 if len(word_averages) > 7 else 0

            # Extends the limit of the x axis if the data does not fit evenly
            if extra_tick != 0:
                plt.xlim(0, len(word_averages) + extra_tick)

            # Correctly formats the x ticks
            plt.xticks(numpy.arange(0, len(word_averages) + tick_step, tick_step), range(start, end + tick_step, tick_step))

            # Sets so that ticks show up on the top and right of the graph and to include a slight y axis margin
            plt.tick_params(direction="in", top=True, right=True)
            plt.margins(0, 0.2)

            # Displays the plot
            plt.show()


if __name__ == '__main__':
    main()
