

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # Child classes will override this method to render themselves as HTML.
    def to_html(self):
        raise NotImplementedError("This method is not implemented.")
    

    # Create a props_to_htmml(self) method. It should return a string that represents the HTML attributes of the node. For example if self.props is:    {
    # "href": "https://www.google.com",
    # "target": "_blank",
    #     }
    # Then self.props_to_html() should return:                                  # href="https://www.google.com" target="_blank"
    # Notice the leading spaces before href and before target. This is important. HTML attributes are always separated by spaces.
    def props_to_html(self):
        # List comprehension instead of a loop
        prop = "".join(f' {prop}="{self.props[prop]}"' for prop in self.props)
        return prop

    # Add a __repr__(self) method. Give yourself a way to print an HTML object and see its tag, value, children, and props. This will be uselful when debugging.
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    

# Create a child class of HTMLNode called 'LeafNode'. Its constructor should differ slightly form  the HTMLNode because:
#       It should not allow for any children
#       The 'value' data member should be required(and tag even though the tag's value may be None)
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Use the 'super()' function to call the constructor of the HTMLNode class.
        super().__init__(tag, value, None, props)
        
       

        # Add a .to_html() that renders a leaf node as an HTML string (by returning a string).
        # IF the leaf node has no value, it should raise a ValueError
        # IF there is no tag (it's None) the value should be returned as raw text
        # Otherwise, it should render an HTML tag.
    
    def to_html(self):
        if len(self.value) == 0:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            # print(self.value)
            return self.value
        # Check if there is a dictionary in self.props
        if self.props != None:
            print(f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")

            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        # print(f"<{self.tag}>{self.value}</{self.tag}>")
        # Else returns a tag with no link
        return f"<{self.tag}>{self.value}</{self.tag}>"


# Create another child class of 'HTMLNode' called 'ParentNode'. Its constructor should differ from HTMLNode in that:
# . The 'tag' and 'children' arguments are not optional
# . It doesn't take a value arguent
# . 'props' is optional
# . (It's the exact opposite of the LeafNode class)
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

# Add a .to_html method
# 1. If the object doesn't have a tag, raise a ValueError.
# 2. If the children is missing value, raise a ValueError with a different message.
# 3. Otherwise return a string representing the HTML tag of the node and its children. This should be a recursive method (each recursion being called on a nested child node). I iterated over all the children and called 'to_html'  on each, concatenating the result and injecting them between the opening and closing tags of the parent.
    def to_html(self):
        if self.tag == 'None':
            raise ValueError("The tag is required")
        elif self.children == None:
            print(f'this is the children: {self.children}')
            raise ValueError("Children is required")
        # Create a variable to accumulate the children string, create a recursion that iterates ober the children and call 'to_html' on each accumulating the result in said variable, return the string between the opening and closing parent tags.
        # Todo This works!
        # If there is something I would to different about this recursion is maybe "".join(node.to_html() for node in self.children)
        # A little list comprehension instead of a loop that recurses on the self.child and applies to_html of the child class.
        result = "".join(child.to_html() for child in self.children)
       
    #    Todo, one miss I had that I would have caught had I run more tests is not adding props to the return... add them tomorrow. props goes inside the first tag e.g '<a href:link https://www.google.com> 'whatever' </a>
        print(f"<{self.tag}>{result}</{self.tag}>")
        return f"<{self.tag}>{result}</{self.tag}>"


        

node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
).to_html()



    
# leaf = [LeafNode("b", "Bold text"),
#         LeafNode(None, "Normal text"),
#         LeafNode("i", "italic text"),
#         LeafNode(None, "Normal text"),]
# for x in leaf:
#     x.to_html()