import unittest

# This test creates two TextNode objects with the same properties and asserts that they are equal. Notice the missing 'url' argument which should have a default value of Nonde. If you run your test with ./test.sh, you should see that the test passes.

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    # Todo When creating a test method the naming of the methods in your TestTextNode matter. When you're working with Python 'unittest' framework, for the framework to discover and execute  your unit test methods they need to start with the prefix 'test_'
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_more_eq(self):
        node3 = TextNode("Testing equality of nodes", TextType.LINK, "https://www.test.com")
        node4 = TextNode("Testing equality of nodes", TextType.LINK, "https://www.test.com")
        self.assertEqual(node3, node4)
    
    def test_not_equal(self):
        node5 = TextNode("Equally guilty!", TextType.IMAGE, )
        node6 = TextNode("Equally guilty!", TextType.ITALIC)
        self.assertNotEqual(node5, node6)


if __name__ == "__main__":
    unittest.main()

