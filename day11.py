#!/bin/python3
"""
Implement an autocomplete system. That is, given a query string s and a set
of all possibly query strings, return all strings in the set that have s as
a prefix.

For example, given the query string de and the set of strings [dog, deer,
deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data setructure
to speed up queries.
"""
def add_word_to_trie(w, trie):
    # base case
    if not w:
        return
    
    if w[0] not in trie:
        trie[w[0]] = dict()
        
    # continue with next characters until base case
    trie[w[0]] = add_word_to_trie(w[1:], trie[w[0]])

    return trie

def setup_trie(d):
    trie = dict()
    
    for word in d:
        trie = add_word_to_trie(word, trie)
        
    return trie

def get_completions(trie):
    completions = []

    # loop through tree and collect characters at level
    for ch in trie:
        
        # if subtrie, go down
        if trie[ch]:
            sub_completions = get_completions(trie[ch])

            for sc in sub_completions:
                completions.append(ch + sc)
        else:
            completions.append(ch)

    return completions

def get_autocomplete(s, dictionary):
    # as datastructure I use a trie, prefix search and compression tree formed
    # as dictionary of dicitonaries in python
    trie = setup_trie(dictionary)
    
    # perform a fast search if words are in the dictionary that start with
    # the prefix string
    subtrie = trie
    for ch in s:
        if ch not in subtrie:
            return []
        
        subtrie = subtrie[ch]
        
    # if we land here, there are words present we need to capture and
    # return 
    completions = get_completions(subtrie)
    
    # as we operate on the relevant subtree, we need to expand the completions
    # with the prefix to get the actual words
    completions = [s + w for w in completions]

    return completions

if __name__ == '__main__':
    print(get_autocomplete('de', ['dog', 'deer', 'deal']))
    print(get_autocomplete('de', []))