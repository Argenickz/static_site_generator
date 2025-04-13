from textnode import TextNode, TextType
from functools import reduce
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """"This function takes nodes as list [node], delimiter(`, *, _) and TextType"""
    # Create a list to catch all the new nodes:
    new_nodes = []
    # Let's run a loop with a bunch of conditions for the nodes:
    # The 'node' is going to be a 'TextNode' object so make sure to get a hold of the values 'e.g. node.string'.
    for node in old_nodes:
        accepted_delimiters = ["`", "**", "*", "_"]
        if node.text_type != text_type.text:
            new_nodes.append(node)
        if  delimiter not in accepted_delimiters:
            raise Exception("the delimiter must match valid options, e.g. `, *, or _")
        node_text = node.text
        delimiter_start_index = node_text.index(delimiter)
        delimiter_end_index = node_text.index(f"{delimiter} ") + 1
        print(f'this is the start index: {delimiter_start_index}')
        print(f"this is the end index: {delimiter_end_index}")
        code_block = node_text[delimiter_start_index:delimiter_end_index]
        print(f"this is the code block: {code_block}")

        

# Todo I need some sort of logic to know what Text_Type to apply
#Perhaps a match with the text type that applies the text type
# transfer the logic so far from split_nodes_delimiter to a helper function
# Create match statements in split_nodes_delimiter

# Todo, this could be the logic:
# `if code_block.strip(delimiter) == (a loop of node text split into items at the delimiter)`, Then apply the texttype.() equal to the delimiter match per the match case.
# ~ Open a new file, don't delete this code, use this as reference.
    
       


node = TextNode("This is a test **code block** word", TextType.text)
split_nodes_delimiter([node], '*', TextType.text)
#


# Try find instead of index?

# Get the index of the starting delimiter position
code_start_index = node.text.index('*')
# Get the index of the ending delimiter position, add 1 for index position
code_end_index = node.text.index('* ') + 1

# Get the code block between the starting and ending positions of the delimiter indexes
code_block = node.text[code_start_index:29]

# print(f'this is the code {code_block}')

# Split the rest of the code at the delimiter, this eliminates the delimiter
rest_of_text = node.text.split(code_block)
# print(rest_of_text)


# words = "This is text with a `code block` word"

# The idea is to split this string into a list of 3 items where:              'This is a text with a' is item 0                                               `code block` is item 1                                                    'word' is item 2

# word_list = words.split('`')

# print(word_list)
# node = "TextNode"
# lst = []
# for i in word_list:
#     lst.append(f"{node}({i})")

# print(lst)