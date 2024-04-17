class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text 
        self.text_type = text_type
        self.url = url

    def __eq__(self, __value: object):
        return self.text == __value.text and self.text_type == __value.text_type and self.url == __value.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}" + ("" if self.url is None else f", {self.url}") + ")"
