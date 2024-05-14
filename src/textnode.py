class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text 
        self.text_type = text_type
        self.url = url

    def __eq__(self, __value: object):
        return self.text == __value.text and self.text_type == __value.text_type and self.url == __value.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}" + ("" if self.url is None else f", {self.url}") + ")"
    

    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        text_type_text = "text"
        text_type_bold = "bold"
        text_type_italic = "italic"
        text_type_code = "code"
        new_node_list = []
         
        for old_node in old_nodes:
            if old_node.text_type != "text":
                new_node_list.append(old_node)
            else:
                text:str = old_node.text
                start_index = text.find(delimiter)
                closing = text.find(delimiter, start_index + len(delimiter))
                if start_index == -1 or closing == -1:
                    raise ValueError("Invalid Markdown syntax: Missing closing delimiter")

                new_nodes = old_node.text.split(delimiter)
                for split_node in new_nodes:
                    if split_node == new_nodes[0] or new_nodes[2]:
                        new_node_list.append(TextNode(split_node, "text"))
                    else:
                        new_node_list.append(TextNode(split_node, text_type))

        return new_node_list