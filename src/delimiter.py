# Import TextNode, TextType from textnode
from pprint import pprint
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    accepted_delimiters = ["`", "**", "*", "_"]
    for node in old_nodes:
        if node.text_type != text_type.text:
            new_nodes.append(node)
        if delimiter not in accepted_delimiters:
            raise Exception("The delimiter must match valid options")
        node_text = node.text
        delimiter_start_index = node_text.index(delimiter)
        delimiter_end_index = node_text.index(f"{delimiter} ")
        code_block = node_text[delimiter_start_index:delimiter_end_index]
        

        text_list = node_text.split(delimiter)
        for text in text_list:
            if text == code_block.strip(delimiter):
                new_nodes.append(TextNode(text, text_type))
            else:
                new_nodes.append(TextNode(text, text_type.text))

        # Split the text at the delimiter, run an inner loop for that list, if the text matches (the code block stripped off the delimiter), then apply the type text in the argument to that, else apply typetext.text to the text, (make sure to append this to the new nodes list)




    # print(
    #     f"This is the start index: {delimiter_start_index}\n"
    #     f"This is the end index: {delimiter_end_index}\n"
    #     f"This is the code block: {code_block}\n"
    #     f"This is the text list: {text_list}\n"
    # )
    pprint(new_nodes)
        

test = [
    TextNode("This is text with a ", TextType.text),
    TextNode("bolded phrase", TextType.bold),
    TextNode(" in the middle", TextType.text),
]
pprint(test)




print('\n')






# Todo I don't need to match text type to know what text type to apply, that text type is passed in the function calling already.





# This is the node example to work with
node = TextNode("This is a **dark** word", TextType.text)
split_nodes_delimiter([node], "**", TextType.bold)