from enum import Enum
from htmlnode import LeafNode
# Create an enum called 'TextType'. It should have all the types mentioned in the course
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

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
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {'href': text_node.url})   
        case TextType.IMAGE:
            
            # Passed the text_node as index to get two values
            return LeafNode("img", "", {"src":text_node.url, "alt": text_node.text})
        case _:
            return 'not a match'
