from enum import Enum
from htmlnode import LeafNode
# Create an enum called 'TextType'. It should have all the types mentioned in the course
class TextType(Enum):
    text = "text"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"

# Create a class called 'TextNode'. It should have 3 properties that can be set in the constructor:
#   self.text: The text content of the node
#   self.text_type: The type of text this node contains which is a member of the TextType enum.
#   self.url: The url of the link or image, if the text is a link. Default to None if nothing is passed in. 
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


#   Create an __eq__ method that returns True if all of the properties of two TextNode oobjects are the equal.
    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
              )

# Create a __repr__ method that returns a string representation of the 'TextNode' object. It should look like this:
#  TextNode(TEXT, TEXT_TYPE, URL) Where those values are representations of the text, text_type and url properties respectively.
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


# Write a function
# def text_node_to_html(text_node):
# It should handle each type of the TextType enum. If it gets a TextNode that is none of those types, it should raise an exception. Otherwise, it should return a new leafnode object.
# TextType.TEXT: This should return a LeafNode with no tag, just raw text.
# TextType.BOLD: This should return a LeafNode with a 'b' tag and the text.
# TextType.ITALIC: 'i' tag and text
# TextType.CODE: 'code' tag and text
# TextType.LINK: 'a' tag, anchor text, and 'href' prop
# TextType.IMAGE: 'img' tag, empty string value, 'src' and 'alt' props ('src' is the image URL, 'alt' is the alt text)

# Todo Working so far
def text_node_to_html(text_node):
    # Match the text type of the node object.
    match text_node.text_type:
        # For the text return a LeafNode with no tag, just raw text
        case TextType.text:
            return LeafNode(None,text_node.text)
        case TextType.bold:
            return LeafNode("b", text_node.text)
        case TextType.italic:
            return LeafNode("i", text_node.text)
        case TextType.code:
            return LeafNode("code", text_node.text)
        case TextType.link:
            return LeafNode("a", text_node.text, text_node.url)   
        case TextType.image:
            return LeafNode("img", text_node.text, text_node.url)
        case _:
            return 'not a match'
        
# Todo Reproduce for the rest
# node = TextNode('this is a node', TextType.text)
# html_node = text_node_to_html(node)
# print(html_node.tag)
# text test: .to_html returns a string. 
# print(text_node_to_html(TextNode('just raw text', TextType.text)).to_html())
# print(text_node_to_html(TextNode("text in bold tags", TextType.bold)))
# print(text_node_to_html(TextNode("text in italic tags", TextType.italic)))
# print(text_node_to_html(TextNode("text in code tags", TextType.code)))
print(text_node_to_html(TextNode("some anchor text", TextType.link, {'href': 'www.damn.com'})).to_html())
# print(text_node_to_html(TextNode("", TextType.image, {'src': 'www.damn.com', 'alt': 'alternative image text'})))



