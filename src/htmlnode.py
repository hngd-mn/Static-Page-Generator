class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_attributes = ''
        for prop, value in self.props.items():
            html_attributes += f' {prop}="{value}"'

        return html_attributes.strip()
    
    def __eq__(self, __value: object):
        return self.tag == __value.tag and self.value == __value.value and self.children == __value.children and self.props == __value.props
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
       
    def to_html(self):
        if self.tag is None:
            return self.value
        elif self.tag == "img":
            return f'<{self.tag}{self.props_to_html()}>'
        elif self.value is None:
            raise ValueError("Leaf nodes must have a value")
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, children, props)

    def to_html(self):
        result = ""
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if not self.children:
            raise ValueError("Parent nodes must have children")
        #for child in self.children:
            #result = result + f'{child.to_html()}'
        #return f'<{self.tag}>' + result + f'</{self.tag}'