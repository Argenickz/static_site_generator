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
            return LeafNode("a", text_node.text, {'href': text_node.url})   
        case TextType.image:
            
            # Passed the text_node as index to get two values
            return LeafNode("img", "", {"src":text_node.url, "alt": text_node.text})
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
# print(text_node_to_html(TextNode("some anchor text", TextType.link, 'www.yes.com')).to_html())

# passed in the url as a list to get the index values
# print(text_node_to_html(TextNode("the iimage test", TextType.image, 'www.image.com')).to_html())



# Todo boots pseudo code:
"""
Ah, I see you're working on the split_nodes_delimiter function. Let me help you work through some issues I notice:

When checking for text_type.text, you're using lowercase, but it should likely be TextType.TEXT (uppercase).

Your approach to finding the delimiter indices is problematic. The index() method will throw an error if the delimiter isn't found, and using index(f"{delimiter} ") assumes the delimiter is always followed by a space, which isn't always true.

You're checking if the delimiter is in the accepted list, but this check should happen before you try to process the node.

Your approach with code_block and splitting by delimiter needs refinement. Let's think about this differently:

What if we consider splitting the text this way:

Find pairs of delimiters (start and end)
Split the text into three parts: before the first delimiter, between delimiters, and after the second delimiter
Create appropriate TextNodes for each part
How would you handle a case like: "This is text with a code block word"?



Boots
maybe using split(delimiter, maxsplit=1)

Boots
That's a clever approach to consider! Using split(delimiter, maxsplit=1) will split the string at the first occurrence of the delimiter, which could help you get the "before" part and "rest" of the string.

Let's think through the steps:

If we find the first delimiter and split at that point, we get:

"This is text with a " (before part)
"code block` word" (rest of the string)
Then we need to find the closing delimiter in the "rest" part and split again:

"code block" (the content we want to mark as code)
" word" (after part)
Let's try to refactor your approach. Consider this pseudocode:

for each node in old_nodes:
    if node is not text type:
        add node to new_nodes as-is
        continue
    
    text = node's text
    
    while delimiter exists in text:
        split text at first delimiter into before_part and rest
        if delimiter doesn't exist in rest:
            raise exception (no closing delimiter)
        
        split rest at first delimiter into content and after_part
        
        add TextNode(before_part, TextType.TEXT) to new_nodes
        add TextNode(content, text_type) to new_nodes
        
        text = after_part (continue processing the remaining text)
    
    if text is not empty:
        add TextNode(text, TextType.TEXT) to new_nodes

This approach handles one pair of delimiters at a time, processes it, and then continues with the remaining text. What do you think of this approach?
"""