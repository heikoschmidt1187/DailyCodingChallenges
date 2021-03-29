#!/bin/python3
"""
Given a dictionary of words and a string made up of those words (no spaces), return
the original sentence in a list. If there is more than one possible reconstruction,
return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string
"thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string
"bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
['bedbath', 'and', 'beyond'].
"""

def find_sentence(s, dictionary):
    # will hold the start index and the matching word
    starts = {0: ''}

    # check char by char
    for i in range(len(s) + 1):
        new_starts = starts.copy()

        # go over the starts we already have and try to 
        # match next word
        for start_index, _ in starts.items():
            word = s[start_index:i]

            # if we find a word from the dict, we add it as
            # a new start
            if word in dictionary:
                new_starts[i] = word

        starts = new_starts.copy()
        
    result = []
    current_length = len(s)

    # build the resulting list in reverted order
    if current_length not in starts:
        return None

    while current_length > 0:
        word = starts[current_length]
        current_length -= len(word)
        result.append(word)

    return list(reversed(result))

if __name__ == '__main__':
    """
    Test 1:
    words = ['quick', 'brown', 'the', 'fox']
    string = 'thequickbrownfox'
    """

    words = ['quick', 'brown', 'the', 'fox']
    string = 'thequickbrownfox'

    """
    Test 2
    words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    string = 'bedbathandbeyond'
    """
    
    print(find_sentence(string, words))