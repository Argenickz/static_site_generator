import unittest

from htmlnode import LeafNode, ParentNode

# Testing LeafNode class
class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a call to the color blind")

        self.assertEqual(node.to_html(), "<p>This is a call to the color blind</p>")

        self.assertNotEqual(node.to_html(), "<div> This is a call to the color blind</div>")

        
    def test_more(self):
        node = LeafNode(None, 'some plain text')
        self.assertEqual(node.to_html(), 'some plain text')
    
    
    def test_what(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
# ==============================================================

# Testing ParentNode class
class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
# Todo Write the rest of the tests tomorrow but submmit tonight and commit/push.



if __name__ == "__main__":
    unittest.main()
