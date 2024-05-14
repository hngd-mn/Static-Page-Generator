import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from htmlnode import text_node_to_html_node


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
            node7 = ParentNode([LeafNode("b", "Bold text"), LeafNode("c", "Italic text")], None)
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
        node9 = ParentNode([LeafNode("b", "Bold text"), LeafNode("c", "Italic text")], "z")
        assert node9.to_html() == "<z><b>Bold text</b><c>Italic text</c></z>"

# text_node_to_html_node tests:

    def test_eq10(self):
        class MockTextNode:
            def __init__(self, text_type, text, url=None):
                self.text_type = text_type
                self.text = text
                self.url = url

# Test cases
        test_cases = [
            MockTextNode("text", "Just some text"),
            MockTextNode("bold", "Bold text"),
            MockTextNode("italic", "Italic text"),
            MockTextNode("code", "Code snippet"),
            MockTextNode("link", "Click here", "https://example.com"),
            MockTextNode("image", "An image", "https://example.com/image.png")
        ]

        for case in test_cases:
            try:
                node = text_node_to_html_node(case)
                print(f"Success: {case.text_type} -> {node}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    unittest.main()