

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
# Todo I'm not entirely sure I've created this class child correctly. summit the test and compare to solution.
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Use the 'super()' function to call the constructor of the HTMLNode class.
        super().__init__(tag, value,None, props)
        
       

        # Add a .to_html() that renders a leaf node as an HTML string (by returning a string).
        # IF the leaf node has no value, it should raise a ValueError
        # IF there is no tag (it's None) the value should be returned as raw text
        # Otherwise, it should render an HTML tag.
    
    def to_html(self):
        if len(self.value) == 0:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            print(self.value)
            return self.value
        # Check if there is a dictionary in self.props
        if self.props != None:
            print(f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")

            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        print(f"<{self.tag}>{self.value}</{self.tag}>")
        # Else returns a tag with no link
        return f"<{self.tag}>{self.value}</{self.tag}>"



