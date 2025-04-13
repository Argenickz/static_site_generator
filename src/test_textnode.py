import unittest
from textnode import TextNode, TextType, text_node_to_html

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


    def test_text(self):
        node = TextNode("This is a text node", TextType.text)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, None)
        self.assertEqual(text_node_to_html(TextNode("some anchor text", TextType.link, 'www.damn.com')).to_html(), '<a href="www.damn.com">some anchor text</a>'  )
    
    def test_tags(self):
        node = TextNode("some italic text", TextType.italic)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "i")

    def test_image_link(self):
        node = TextNode("this is the text", TextType.image, ['www.image.com', 'the image'])
        html_node = text_node_to_html(node)

if __name__ == "__main__":
    unittest.main()

