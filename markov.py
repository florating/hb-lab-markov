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
    words_list = text_string.split()        # words_list is a list of strings (words) from input text_string
    for i in range(0, len(words_list), 2):  # use range(start, stop, step)
        j = i + 1
        if j < len(words_list):
            key = (words_list[i], words_list[j])
            # word_pair = words_list[i] + ' ' + words_list[j]
        else:
            key = (words_list[i], )
            # word_pair = words_list[i] + ' ' + '_'
        
        if j + 1 < len(words_list):
            chain_word = words_list[j + 1]
        else:
            chain_word = None
        # print(f'chain_word = {chain_word}')
        chains[key] = chains.get(key, list())
        # print(f'chains[key] for key = {key} is {chains[key]}')
        chains[key].append(chain_word)      # why can't I combine this with the code one line above?
    return chains


def make_text(chains):
    """Return ____ after: Make a new list to link dict key + value
    
    INPUT: 
    OUTPUT: 
    """

    """
    INSTRUCTIONS:
    ## GOAL: So you’ve created a valid dictionary, and it’s getting passed into the function that will create our fake text.
    # INPUT: new dictionary created using make_chains(text_block_string)

    # chains (dictionary) is passed into a new function (make_text) (+ more arguments?)

    ## TO GENERATE CHAIN OF FAKE TEXT:
        To make a chain of fake text, we need to start with a link.
        A link in our case is a key from our dictionary and a random word from the list of words that follow it.
        # start with a link (make a function call and passing a link into it?)
        # link = key (tuple of strings) from chains (dictionary) and a random word (string) from the paired value (list of strings) within chains

        Put that link in some kind of container (the skeleton file suggests adding each word to a list and joining the list into a string at the end).
        # container(link) --> container(key_tup and rand_word_string)

        # join the list into a string at the end

        Once we have our first link, we can add another to it,
            and we can repeat the following process to add more:

        1. Make a new key out of the second word in the first key and the random word you pulled out from the list of words that followed it.
        2. Look up that new key in the dictionary, and pull a new random word out of the new list. #storing this value in a list??
        3. Keep doing that until your program raises a KeyError.

        Well shoot, the KeyError broke our program. How about we keep trying to look for the existence of each key before trying to make a link, and then stop once the newest key is no longer in the dictionary?

    Return a string of the words you’ve pulled out.
    Remember, when using the supplied green_eggs.txt file, if the text generation is working, it will always end with the words “Sam I am?”
    """

    words = [] #new generated word pairs

    return ' '.join(words)


def fxn_1(word_strings):
    """
    Make a new key out of the second word in the first key and the random word you pulled out from the list of words that followed it.

    new_key = (the second word in the first key) and (the random word you pulled out from the list of words that followed it)

    PARAMETERS: 
        word_strings (data type): description of the value it contains

    dictionary key, value list

    EFFECT: generate dictionary key, generate word from value list

    RETURN:
    """

    for 
    
    pass


def test():
    string = 'Would you could you in a house?'
    mydict = make_chains(string)
    print(mydict)



input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# print(chains)

"""

# Produce random text
random_text = make_text(chains)

print(random_text)
"""
