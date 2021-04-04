#!/bin/python3
"""
Write an algorithm to justify text. Given a sequence of words and an integer line
length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There
should be at least one space between each word. Pad extra spaces when necessary
so that each line has exactly length k. Spaces should be distributed as equally
as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side
with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and
k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

def get_line(c_line, c_len):
    # fit additional spaces
    missing_spaces = k - c_len
    
    # only preprocess if there are missing spaces
    if missing_spaces:
        if len(c_line) == 1:
            # if only one word in line, append spaces to the end
            c_line.append(missing_spaces * ' ')
        else:
            # distribute evenly by adding the amount
            # of spaces to the existing ones
            existing_spaces = len(c_line) // 2
            
            # get the amount of spaces to append on EVERY existing space
            append_all = missing_spaces // existing_spaces
            
            # there may be a rest of spaces to fill up from left
            append_rest = missing_spaces % existing_spaces

            # loop over spaces and append them with the correct amount
            for i in range(len(c_line)):
                if c_line[i] == ' ':
                    # append spaces all spaces get
                    c_line[i] += append_all * ' ';

                    if append_rest:
                        # distribute rest of spaces from left on
                        c_line[i] += ' '
                        append_rest -= 1
            
    return ''.join(c_line)

def justify(words, k):
    lines = []

    cur_line = []
    cur_len = 0
    
    for w in words:
        # check if next word fits in line inkl. leading space
        if cur_len + len(w) + 1 > k:
            # join line words into one line
            lines.append(get_line(cur_line, cur_len))
            
            # reset for next round
            cur_line = [w]
            cur_len = len(w)
        else:

            cur_len += len(w)

            # prepend with space if not first word
            if len(cur_line) > 0:
                cur_len += 1
                cur_line.append(' ')

            # append the actual word
            cur_line.append(w)
            
    if cur_len > 0:
        lines.append(get_line(cur_line, cur_len))

    return lines

if __name__ == '__main__':
    #words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the"]
    k = 16
    
    print(justify(words, k))