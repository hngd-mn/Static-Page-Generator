import unittest

from textnode import TextNode
from textnode import split_nodes_delimiter



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev/")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev/")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is text with a `code block` word", "text")
        print(split_nodes_delimiter([node], "'", "code"))

if __name__ == "__main__":
    unittest.main()