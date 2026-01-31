from enum import Enum

TextType = Enum('Type', ['plain', 'bold', 'italic', 'code', 'link', 'image']) 

class TextNode:
    def __init__(self, text, TextType, URL):
        self.text = text
        self.text_type = TextType
        self.url = URL

    def __eg__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
