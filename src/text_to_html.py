from htmlnode import ParentNode, LeafNode, HTMLNode
from textnode import TextNode


def text_node_to_html(text_node: TextNode) -> HTMLNode:
    match text_node.text_type:
        case "text":
            return LeafNode(value=text_node.text)
        case "bold":
            return LeafNode(tag="b", value=text_node.text)
        case "italic":
            return LeafNode(tag="i", value=text_node.text)
        case "code":
            return LeafNode(tag="code", value=text_node.text)
        case "link":
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case "image":
            return LeafNode(tag="img", value=" ", props={"src": text_node.ulr, "alt": text_node.text})
        case _:
            raise ValueError(f"invalid type: {text_node.text_type}")