from textnode import TextType, TextNode

# Create a main() function in main.py and call it. The function should create a new TextNode object with some dummy values. Print the object and make sure it looks like you'd expect:                                                   (TextNode(This is some anchor text, link, https://www.boot.dev))
def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://wwww.boot.dev")
    print(text_node)



main()


