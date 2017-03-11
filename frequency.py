""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg

Author: Gretchen Rice
Date: March 11, 2017

"""

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    #opens text and strips the beginning introduction to Project Gutenberg
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
      curr_line += 1
    lines = lines[curr_line+1:]

    # splits into list of just words
    split_lines = [i.split(' ', 1)[0] for i in lines]

    # strips words of unwanted characters and adds to list
    stripped = []
    for word in split_lines:
        word = word.lower().strip(" ")
        # makes sure list doesn't include empty strings or new line strings
        if word != '\n' and word != '':
            #for some reason this won't strip quotation marks
            stripped.append(word.strip(" !#$%&'\"()*+,-./:;<=>?@[\]^_`{|}~\r\n"))

    return stripped


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """

    # creates a histogram of the list of words
    hist = dict()
    for c in word_list:
        hist[c] = hist.get(c, 0) + 1

    # orders the hist by word frequency
    ordered_by_frequency = sorted(hist, key=hist.get, reverse=True)

    #creates a list of top n words
    top = ordered_by_frequency[:n]

    return top

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    word_list = get_word_list('Pinocchio.txt')
    print(get_top_n_words(word_list, 100))
