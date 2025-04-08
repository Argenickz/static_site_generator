import unittest

from htmlnode import LeafNode

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

    

if __name__ == "__main__":
    unittest.main()
