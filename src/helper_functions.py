import collections
import sys


def read_file(filename: str) -> dict:
    file = ""

    try:
        file = open("../" + filename)

    except FileNotFoundError:
        sys.stderr.write("Error: " + filename + " does not exist!\n")
        exit(1)

    Word = collections.namedtuple("Occurrence", ("word", "year", "usage"))
    occurrences = {}

    for line in file:
        components = line.strip().split(',')
        entry = Word(components[0].strip(), components[1].strip(), components[2].strip())

        if entry.word in occurrences:
            occurrences[entry.word].append((entry.year, entry.usage))
        else:
            occurrences[entry.word] = [(entry.year, entry.usage)]

    return occurrences
