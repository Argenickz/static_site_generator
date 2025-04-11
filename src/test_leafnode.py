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

        parent_node1 = ParentNode("a", [LeafNode('p', 'this right here')], {"href": "https://www.test.com"})
        self.assertEqual(parent_node1.to_html(), '<a href="https://www.test.com"><p>this right here</p></a>')

        
      

    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

        # ParentNode expects the children parameter to be a list of nodes
    def test_nested_parent_node(self):
        nested_parent1 = LeafNode("div", "parent node one")
        nested_parent2 = ParentNode("p", [nested_parent1])
        parent_node = ParentNode("b", [nested_parent2])
        self.assertNotEqual(parent_node.to_html(), 'whatever')

        

if __name__ == "__main__":
    unittest.main()
