from textnode import TextNode


def main():
    testnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    return print(testnode.__repr__())

main()