"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.

    LINK: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    """
    the_file = open(file_path)
    file_string = the_file.read()
    the_file.close()
    return file_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words_list = text_string.split()    # words_list is a list of strings (words) from input text_string
    for i in range(0, len(words_list), 2):      # use range(start, stop, step)
        j = i + 1
        if j < len(words_list):
            key = (words_list[i], words_list[j])
            # word_pair = words_list[i] + ' ' + words_list[j]
        else:
            key = (words_list[i], )
            # word_pair = words_list[i] + ' ' + '_'
        
        if j + 1 < len(words_list):
            chain_word = words_list[j + 1]
            # print(f'chain_word = {chain_word}')
            chains[key] = chains.get(key, list())
            # print(f'chains[key] for key = {key} is {chains[key]}')
            chains[key].append(chain_word)      # why can't I combine this with line 61?
    return chains


def make_text(chains):
    """Return text from chains.
    
    INPUT: 
    OUTPUT: 
    """

    words = []

    # your code goes here

    return ' '.join(words)


def test():
    string = 'Would you could you in a house?'
    mydict = make_chains(string)
    print(mydict)


"""
input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
"""
