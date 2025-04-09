import unittest
from textnode import TextNode, TextType

# This test creates two TextNode objects and asserts that they are equal. Notice the missing url argument which should default to None. If you run the test with ./test.sh you should see that the test passes.
# Note! For the text to be discoveret bhy the unittest they need to be prefixed with the word 'test_'.
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node3 = TextNode("this is crazy", TextType.italic)
        node4 = TextNode("this is crazy", TextType.italic)
        self.assertEqual(node3, node4)
    
    def test_not_the_same(self):
        node5 = TextNode("We're not the same you and I", TextType.text, "www.notthesame.com")
        node6 = TextNode("Not the same at all", TextType.bold)
        self.assertNotEqual(node5, node6)

if __name__ == "__main__":
    unittest.main()

