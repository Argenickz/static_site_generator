from textnode import TextNode, TextType
from htmlnode import HTMLNode
# Todo
# Import the classes from textnode, I'd suggest to import the classes by name for readability.





# Todo
# Create a 'main()' function in main.py and call it. The function should create a new 'TextNode' object with some dummy values. Print the object, and make sure ir looks like you'd expect, for example: 
#  TextNode (This is some anchor text, link, https://www.boot.dev)

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)

   
main()
