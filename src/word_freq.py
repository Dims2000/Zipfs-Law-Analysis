import matplotlib.pyplot as plt
import helper_functions
import numpy
import argparse
import sys


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("word", help="a word to display the overall ranking of")
    parser.add_argument("-o", "--output", help="display the top OUTPUT (#) ranked words by number of occurrences")
    parser.add_argument("-p", "--plot", help="plot the word rankings from top to bottom based on occurrences", action="store_true")
    parser.add_argument("filename", help="a comma separated value unigram file")

    args = parser.parse_args()

    word = args.word
    word_dict = helper_functions.read_file(args.filename)

    if word not in word_dict:
        sys.stderr.write("Error: " + args.word + " does not appear!\n")
        exit(2)

    word_usage_list = [(word, helper_functions.total_words(tup)) for (word, tup) in word_dict.items()]
    word_usage_list.sort(key=lambda tup: tup[1])
    word_usage_list.reverse()

    limit = len(word_usage_list)

    try:
        if args.output is not None and int(args.output) < len(word_usage_list):
            limit = int(args.output)
    except AttributeError:
        pass

    rank_of_word = str(word_usage_list.index((word, helper_functions.total_words(word_dict[word]))) + 1)
    print(word + " is ranked #" + rank_of_word)

    for index in range(limit):
        print("#" + str(index + 1) + ": " + word_usage_list[index][0] + " -> " + str(word_usage_list[index][1]))

    if args.plot:
        index = numpy.arange(1, len(word_usage_list) + 1)
        plt.loglog(index, [usage for word, usage in word_usage_list], color="green")
        plt.xlabel("Rank of word (\"" + word + "\" is ranked " + rank_of_word + ")")
        plt.ylabel("Total number of occurrences")
        filename = str(args.filename)
        plt.title("Word Frequencies: " + filename.split("/")[1])
        plt.xticks(index)
        plt.tick_params(labelbottom=False)
        plt.margins(0)
        plt.scatter(index[1:-1], [usage for word, usage in word_usage_list[1:-1]], s=10, color="blue")
        plt.scatter(int(rank_of_word), helper_functions.total_words(word_dict[word]),
                    color="red", s=120, marker="*", label=word, zorder=7, edgecolors="black")
        plt.text(int(rank_of_word) + 0.05, helper_functions.total_words(word_dict[word]) + 0.1, word, fontsize=9)
        plt.show()


if __name__ == '__main__':
    main()
