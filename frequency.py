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
    #opens text and strips the introduction and ending to Project Gutenberg
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
      curr_line += 1

    end_line = 0
    while lines[end_line].find('End of the Project Gutenberg EBook of The Adventures of Pinocchio') == -1:
      end_line += 1

    lines = lines[curr_line+1:end_line]

    #converts to lowercase
    lower = []
    for st in lines:
        lower.append(st.lower())

    #removes punctuation
    s = ''
    for line in lower:
        s += ''.join(ch for ch in line if ch.isalpha() or ch == ' ' or ch == '\n')

    # splits into list of just words
    split_lines = s.split()

    return split_lines


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

     # list of words I want to remove form histList
    unwanted = ['a', 'an', 'be', 'and', 'are', 'from', 'for', 'the', 'they',
    'their', "they're", 'then', 'them', 'is', 'if', 'of', 'with', 'to', 'in',
    'was', 'that', 'as', 'at', 'this', 'so', 'had','on', 'it', 'or']

    # removes unwanted words from listHist, creates new list
    wanted = [word for word in ordered_by_frequency if word not in unwanted]

    #creates a list of top n words
    top = wanted[:n]

    return top

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    word_list = get_word_list('Pinocchio.txt')
    print(get_top_n_words(word_list, 100))
