"""From working on make_chains function.

A chain will be a key that consists of a tuple of (word1, word2)
and the value would be a list of the word(s) that follow those two
words in the input text.
"""
def example_while(words_list):
    ## PART A of make_chains function ##
    i = 0
    while i < len(words_list):  
        j = i + 1               
        if j < len(words_list):
            print(f"make regular tuple using index i = {i} and j = {j}")
        else:
            print(f"make tuple with empty second spot using index i = {i} only")            
        i += 2
    print("I'm done.")

    OUTPUT:
    ('1', '2') done
    ('3', '4') done
    ('5', ) done

        # use range(start, stop, step) in some kind of loop
    for i in range(0, len(words_list), 2):
    ## example ##

    INPUT: ['1', '2', '3', '4', '5']
    
    OUTPUT:
    ('1', '2')
    ('3', '4')
    ('5', )


    ########
    ## PART B of make_chains function##
    # and the value would be a list of the word(s) that follow 
    # those two words in the input text.
        # option 1: make a list of keys, iterate through it after this for loop (in make_chains function) is done to do part B
        # option 2: use this for loop to create a list of words that follow this tuple (use a helper function?)

    # return dictionary of Markov chains.

    ## EXAMPLE (Part B) ##
    INPUT: ['1', '2', '3', '4', '5']
    i = 0               # words[i] = first word in pair
    j = i + 1 = 1       # words[j] = second word in pair
    (k) = j + 1 = 2     # words[k] = word to add to the list of stuff for Markov chain

        

