import argparse
import matplotlib.pyplot as plt
import numpy
import util
import sys


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--output", help="display the average word lengths over years", action="store_true")
    parser.add_argument("-p", "--plot", help="plot the average word lengths over years", action="store_true")
    parser.add_argument("start", help="the starting year range")
    parser.add_argument("end", help="the ending year range")
    parser.add_argument("filename", help="a comma separated value unigram file")

    args = parser.parse_args()
    filename = str(args.filename)
    start = int(args.start)
    end = int(args.end)

    if start > end:
        sys.stderr("Error: start year must be less than or equal to end year!\n")
        exit(3)

    if args.output or args.plot:
        word_dict = util.read_file(filename)
        average_word_len = {str(year): (0, 0, 0.0) for year in range(start, end + 1)}

        for (word, entry) in word_dict.items():

            for (year, usage) in entry:
                if start <= int(year) <= end:
                    num_of_letters = average_word_len[year][1] + int(usage)
                    word_weight = average_word_len[year][0] + (len(word) * int(usage))

                    average_word_len[year] = (word_weight, num_of_letters, (word_weight / num_of_letters))

        word_averages = {key: average_word_len[key][2] for key in average_word_len.keys()}

        if args.output:
            for key in word_averages:
                print(key + ": " + str(word_averages[key]))

        if args.plot:
            index = numpy.arange(1, len(word_averages) + 1)
            plt.plot(index, word_averages.values(), color="blue", linewidth=0.75)
            plt.xlabel("Year")
            plt.ylabel("Average word length")
            plt.title("Average word lengths from " + str(start) + " to " + str(end) + ": " + filename.split("/")[1])
            plt.xticks(numpy.arange(1, len(word_averages) + 1, 50), (i for i in range(start, end, 50)))
            plt.margins(0)
            plt.show()


if __name__ == '__main__':
    main()
