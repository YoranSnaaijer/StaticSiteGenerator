class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_props = ""
        for key in self.props:
            html_props += f" {key}=\"{self.props[key]}\""
        return html_props

    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps:\n{self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value specified")
        if self.tag == None:
            return self.value
        else:
            if self.props != None:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nProps:\n{self.props}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag specified")
        if self.children == None:
            raise ValueError("No children specified")
        else:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
        if self.props != None:
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_html}</{self.tag}>"

