import unittest
from htmlnode import HTMLNode
# Create some tests for the HTMLNode class (at least 3). Create a few nodes and make sure that the 'props_to_html' method works as expected.

class TestHTMLNode(unittest.TestCase):
    # In this test case we're passing all the arguments in the HTMLNode constructor, notice how we're passing 'None' for the Children argument.
    # Self.props argument is a dictionary.
    def test_eq(self):
        node1 = HTMLNode('<p>', 'some text', None,  {
    "href": "https://www.google.com",
    "target": "_blank",
})
        self.assertEqual(node1.props_to_html(), 
            ' href="https://www.google.com" target="_blank"')
        # ====================================================

#   Todo I don't need to create a bunch of new methods, I can pass all the arguments into this method and then create many assert tests using different values.
    def test_text(self):
        node = HTMLNode('div', 'this is the value', None, {'website': 'google', 'href': 'https://google.com'})


        self.assertEqual(node.tag, 'div')

        self.assertEqual(node.value, 'this is the value')   

        self.assertEqual(node.children, None)

        self.assertNotEqual(node.props_to_html(), 'some random stuff')    

        self.assertEqual(node.props_to_html(), ' website="google" href="https://google.com"')     
     



if __name__ == "__main__":
    unittest.main()

