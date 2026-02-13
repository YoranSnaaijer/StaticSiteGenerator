import unittest
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_type_link(self):
        node = TextNode("Click me", TextType.LINK, "https://example.com")
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "a")
        self.assertEqual(result.value, "Click me")
        self.assertEqual(result.props, {"href": "https://example.com"})
    
    def test_text_type_image(self):
        node = TextNode("Alt text for image", TextType.IMAGE, "https://example.com/image.jpg")
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "img")
        self.assertIsNone(result.value)
        self.assertEqual(result.props, {
            "src": "https://example.com/image.jpg",
            "alt": "Alt text for image"
        })
    
    def test_empty_text(self):
        # Test with empty string
        node = TextNode("", TextType.TEXT)
        result = text_node_to_html_node(node)
        self.assertEqual(result.value, "")
    
    def test_special_characters(self):
        # Test that special characters are preserved
        node = TextNode("<script>alert('xss')</script>", TextType.TEXT)
        result = text_node_to_html_node(node)
        self.assertEqual(result.value, "<script>alert('xss')</script>")
    
    def test_link_with_special_url(self):
        node = TextNode("Link", TextType.LINK, "https://example.com?param=1&other=2")
        result = text_node_to_html_node(node)
        self.assertEqual(result.props["href"], "https://example.com?param=1&other=2")
