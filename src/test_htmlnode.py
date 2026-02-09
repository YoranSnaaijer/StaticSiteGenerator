import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        child_node3 = LeafNode("span", "child3")
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3])
        self.assertEqual(
                parent_node.to_html(),
                "<div><span>child1</span><span>child2</span><span>child3</span></div>"
                )

