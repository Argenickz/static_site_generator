import unittest
from textnode import TextNode, TextType
from pprint import pprint


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not delimiter:
        raise Exception("The delimiter cannot be an empty string")
    new_nodes = []

    for node in old_nodes:
        
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text =  node.text
            while delimiter in text:
                first_split = text.split(delimiter, maxsplit=1)
                first_text = first_split[0]

                rest = first_split[1]

                if delimiter not in rest:
                    raise Exception("no closing delimiter")
                second_split = rest.split(delimiter, maxsplit=1)
                content = second_split[0]
                after_text = second_split[1]
                if first_text:
                    new_nodes.append(TextNode(first_text, TextType.TEXT))
                new_nodes.append(TextNode(content, text_type))

                text = after_text

            if text:
                new_nodes.append(TextNode(text, TextType.TEXT))
    print(new_nodes)
    return new_nodes