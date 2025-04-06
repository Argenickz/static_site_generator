from enum import Enum
# From enum import Enum
# Enums are sets  of symbolic names (members) bound to unique values. Can be iterated over and return its canonical (conforming to a rule or principle) in definition order. Uses call syntax to return members by value. Use index syntax to return members by name.

# Todo
# Crearte an enum called 'TextType'. It should cover all the types of text nodes mentioned in the project.
class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'


# Todo
# Create a class called 'TextNode'. It should have 3 properties that can be set in the constructor:
# self.text: The text content of the node
# self.text_type: The type of text this node contains which is a member of the 'TextType' 
# self.url: The URL of the link or image, if the text is a link. Default to none if nothing is passed
# Note: If you wont be passing an argument, there is no need for parenthesis in the class creation
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    # Todo
    # Create an __eq__ method that returns true if all of the properties of two 'TextNode' objects are equal. Our future unit tests will rely on this method to compare objects.
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    # Todo
    # Create a __repr__ method that returns a string representation of the 'TextNode' object. It should look like this: 'TextNode(TEXT, TEXT_TYPE, URL)
    # You may want to use '.value' on the 'text_type' field to get the string representation of the enum.
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
 

