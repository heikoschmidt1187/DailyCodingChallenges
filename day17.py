#!/bin/python3
"""
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory
subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1
contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file
file2.ext.

We are interested in finding the longest (number of characters) absolute path
to a file within our file system. For example, in the second example above,
the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its
length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the
length of the longest absolute path to a file in the abstracted file system.
If there is no file in the system, return 0.

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""
class Node():
    def __init__(self, name):
        self.name = name
        self.type = 'file' if '.' in name else 'directory'
        self.children = list()
        self.max_len = 0
        
    def __repr__(self):
        return "(name={}, type={})".format(self.name, self.type)
        
def build_graph(glist):
    # edge case - list empty
    if not glist:
        return None
    
    # we build the graph in a recursive manner, so the current root is
    # the first node in the list
    root_node = glist[0][1]
    level = glist[0][0]
    
    # loop over children
    for idx, (lvl, _) in enumerate(glist[1:]):
        # handle the case where the next node is at same or upper level its no subgraph
        if lvl <= level:
            break
        
        # if next node is level deeper, we have a new subgraph to parse
        if lvl == level + 1:
            root_node.children.append(build_graph(glist[idx + 1:]))
            
            # we use the recursion to calculate the max length of the children
            if root_node.children[-1].children or root_node.children[-1].type == 'file':

                # only assign to current max length
                if root_node.children[-1].max_len + len(root_node.children[-1].name) > root_node.max_len:
                    root_node.max_len = root_node.children[-1].max_len + len(root_node.children[-1].name)
        
    # we are a leaf, so return
    return root_node

def get_max_path_len(s):
    # split individual lines
    lines = s.split('\n')
    
    # edge case
    if len(lines) == 0:
        return 0
    
    # if we have lines given, depending on how many \t are present it's
    # defined what sublevel we are -- 0 - root level
    level_nodes = [x.split('\t') for x in lines]
    
    # use the level nodes to build a list that can be fused as graph
    graph_list = [(len(x) - 1, Node(x[-1])) for x in level_nodes]
    g = build_graph(graph_list)
    
    # if no graph is present, empty
    if g is None:
        return 0
    
    # the maximum length is the max length of the graph's root node + its name
    return len(g.name) + g.max_len

if __name__ == '__main__':
    #dir_str ="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" 
    dir_str = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(get_max_path_len(dir_str))