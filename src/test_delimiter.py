import unittest
from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from pprint import pprint




class TestDelimiter(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        
        new_node = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(new_node[0].text_type, node.text_type)
        self.assertEqual(new_node[1].text_type, TextType.CODE)
        

        bold_node = TextNode("**the dark lord** rises **again**!", TextType.TEXT)
        delim = split_nodes_delimiter([bold_node], '**', TextType.BOLD)
        other_bold_node = TextNode("**all** men must **die**", TextType.TEXT)
        new_bold_node = split_nodes_delimiter([bold_node, other_bold_node], "**", TextType.BOLD)
        self.assertEqual(new_bold_node[0].text_type, new_bold_node[4].text_type)
        self.assertEqual(new_bold_node[0].text, 'the dark lord')
        self.assertEqual(new_bold_node[-1].text_type, TextType.BOLD)
        self.assertEqual(new_bold_node[-1].text, 'die')

        code = TextNode("Here's that _fancy_word you wanted", TextType.TEXT)
        new_italic_node = split_nodes_delimiter([code], "_", TextType.ITALIC)
        self.assertEqual(new_italic_node[1].text_type, TextType.ITALIC)
        

if __name__ == "__main__":
    unittest.main()