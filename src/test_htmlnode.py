import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHTMLNode(unittest.TestCase):
# HTMLNode tests:
    def test_eq(self):
        node = HTMLNode("a", "b", "c", "d")
        node2 = HTMLNode("a", "b", "c", "d")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq3(self):
        node3 = HTMLNode(None, None, None, {"href": "https://www.example.com", "target": "_blank"})
        assert node3.props_to_html() == 'href="https://www.example.com" target="_blank"'

# LeafNode tests:

    def test_eq4(self):
        node4 = LeafNode('p', 'This is a test')
        assert node4.to_html() == '<p>This is a test</p>'

    def test_eq5(self):
        node5 = LeafNode(value='Just some text')
        assert node5.to_html() == 'Just some text'

    def test_eq6(self):
        try:
            node6 = LeafNode('p', None)
            node6.to_html()
            raise AssertionError("ValueError was not raised")
        except ValueError:
            pass  # This is expected

# ParentNode tests:

    def test_eq7(self):
        try:
            node7 = ParentNode([LeafNode("b", "Bold text")], None)
            print("test7", node7.to_html())
            raise AssertionError("ValueError was not raised")
        except ValueError:
            pass  # This is expected

    def test_eq8(self):
        try:
            node8 = ParentNode([], "x")
            print("test8", node8.to_html())
            raise AssertionError("ValueError was not raised")
        except ValueError:
            pass  # This is expected

    def test_eq9(self):
        


if __name__ == "__main__":
    unittest.main()