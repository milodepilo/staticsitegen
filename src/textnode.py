from htmlnode import HTMLNode, LeafNode
import re

class TextNode:
    def __init__(self, text: str, text_type: str, url: str = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, __value: object) -> bool:
        if self.text == __value.text and self.text_type == __value.text_type and self.url == __value.url:
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return(f"TextNode({self.text}, {self.text_type}, {self.url})")


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
            return LeafNode(tag="img", value="", props={"src": text_node.ulr, "alt": text_node.text})
        case _:
            raise ValueError(f"invalid type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        elif node.text.count(delimiter) % 2 != 0:
            raise ValueError("invalid markdown only 1 delimiter found")
        else:
            split_text = node.text.split(delimiter)
            for i in range(len(split_text)):
                if i % 2 == 0:
                    split_text[i] = TextNode(split_text[i], "text")
                else:
                    split_text[i] = TextNode(split_text[i], text_type)
            new_nodes.extend(split_text)
    return new_nodes
            
def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def split_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) < 1:
            new_nodes.append(node)
        else:
            for image in images:
                split_text = node.text.split(f"![{image[0]}]({image[1]})", 1)
                new_nodes.append(TextNode(split_text[0], "text"))
                new_nodes.append(TextNode(image[0], "image", image[1]))
                node.text = split_text[1]
    return new_nodes

def split_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) < 1:
            new_nodes.append(node)
        else:
            for link in links:
                split_text = node.text.split(f"[{link[0]}]({link[1]})", 1)
                new_nodes.append(TextNode(split_text[0], "text"))
                new_nodes.append(TextNode(link[0], "link", link[1]))
                node.text = split_text[1]
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, "text")]
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    nodes = split_images(nodes)
    nodes = split_links(nodes)
    return nodes