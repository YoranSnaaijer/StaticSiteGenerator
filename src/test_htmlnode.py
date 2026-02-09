import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
                "BOLD", 
                12, 
                None,
                {"href": "https://www.google.com", "target": "_blank",}
                )
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')

    def test_html_values(self):
        node = HTMLNode(
                "div",
                "Example test",
                "child"
                )
        self.assertEqual(
                node.tag,
                "div"
                )
        self.assertEqual(
                node.value,
                "Example test"
                )
        self.assertEqual(
                node.children,
                "child"
                )
        self.assertEqual(
                node.props,
                None
                )

    def test_html_repr(self):
        node = HTMLNode(
                "H1",
                "Hello world!",
                None,
                {"color": "blue"}
                )
        self.assertEqual(
                node.__repr__(),
                "Tag: H1\nValue: Hello world!\nChildren: None\nProps:\n{'color': 'blue'}") 
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Check this out!", {"href": "https://nu.nl"})
        self.assertEqual(node.to_html(), '<a href="https://nu.nl">Check this out!</a>')
