from enum import Enum

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
