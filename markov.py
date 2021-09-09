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
    """BROKEN! Use make_chains_alt function instead.
    Take input text as string; return dictionary of Markov chains.

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
    print(f"The length of words_list is {len(words_list)}")

    for i in range(0, len(words_list), 2):  # use range(start, stop, step)
        j = i + 1
        if j < len(words_list):
            key = (words_list[i], words_list[j])
            # word_pair = words_list[i] + ' ' + words_list[j]
        else:
            break
            # key = (words_list[i], )
            # word_pair = words_list[i] + ' ' + '_'
        
        if j + 1 < len(words_list):
            chain_word = words_list[j + 1]
            # print(f'chain_word = {chain_word}')
            chains[key] = chains.get(key, list())
            # print(f'chains[key] for key = {key} is {chains[key]}')
            chains[key].append(chain_word)      # why can't I combine this with the code one line above?
        else:
            break
    return chains


def make_chains_alt(text_string):
    """Alternative way!! Check ALL word pairs."""
    chains_dict = {}
    words_list = text_string.split()
    i = 0
    while i + 1 < len(words_list):
        j = i + 1
        k = i + 2
        key = (words_list[i], words_list[j])
        if k >= len(words_list):
            break
        chain_word = words_list[k]
        chains_dict[key] = chains_dict.get(key, [])
        chains_dict[key].append(chain_word)
        i += 1
    return chains_dict


def print_dict(chains_dict):
    """Print dictionary such that each key-value pair takes up one line."""
    for key, value in chains_dict.items():
        print(f"{key}: {value}")


def make_text(chains_dict):
    """Return a randomly generated chain of text based on input from chains_dict .
    
    PARAMETERS:
        chains_dict (dictionary): dictionary where each key is a word pair (tuple) and each associated value is a list of words (list of strings)    
    RETURN: 
        randomly generated string of text
        Note: if using 'green-eggs.txt' as the input file, the text generation will always end with the words "Sam I am?"
    """

    starting_key = choice(list(chains_dict.keys()))
    generated_text_list = [starting_key[0]]
    # print(f"Starting_key = {starting_key}, generated_text_list = {generated_text_list}, and second word is {starting_key[1]}")
    while starting_key[1]:
        generated_text_list.append(starting_key[1])
        starting_key = make_new_key(starting_key, chains_dict)
    return ' '.join(generated_text_list)


def make_new_key(input_key, chains_dict):
    """Return a new link given the initial input_key and the chains dictionary.

    PARAMETERS: 
        input_key (data type): word pair stored as a key in chains_dict
        chains_dict (dictionary): dictionary where each key is a word pair (tuple) and each associated value is a list of words (list of strings)

    EFFECT: 
        Select a random word from list of words associated with input_key
        Create a new key with the second word from input_key and the random word described above.

    RETURN:
        A new key (tuple) to use in the random text generator function.
    """
    word_list = chains_dict[input_key] if input_key in chains_dict else None
    random_word = choice(word_list) if word_list else None
    new_key = (input_key[1], random_word)
    return new_key


def test():
    string = 'Would you could you in a house?'
    mydict = make_chains(string)
    print(mydict)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains_alt(input_text)

## test with: print_dict(chains)

# Produce random text
random_text = make_text(chains)

print(random_text)
