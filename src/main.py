from textnode import TextNode, text_node_to_html, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_images, split_links, text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from blockline import markdown_to_blocks, block_to_block_type,markdown_to_html_node
import block_types

def main():
    # t_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # h_node = LeafNode(tag="a", value="link", props={"href": "https://www.google.com", "target": "_blank"})
    # node1 = HTMLNode(tag='p', value='Hello, world!', props={'id': 'intro', 'class': 'highlight'})
    # l_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    # print(h_node.to_html())
    # node = ParentNode(
    # "p",
    # [
    #     LeafNode("b", "Bold text"),
    #     LeafNode(None, "Normal text"),
    #     LeafNode("i", "italic text"),
    #     LeafNode(None, "Normal text"),
    # ],
    # )

    # print(node.to_html())


    # node = ParentNode("div", None)
    # print(node.to_html())
    # text = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)", text)
    # print(extract_markdown_images(text))
    # # [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
    # # text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    # print(extract_markdown_links(text))
    # # [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
    # print(split_images([text]))
    # text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"

    # node = TextNode(
    # "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    # "text",
    # )
    # new_nodes = split_links([node])
    # print(text_to_textnodes(text))
    md = """# This is a heading

```
This is a paragraph of text. It has some **bold** and *italic* words inside of it.
```

this is a real para

* This is a list item
* This is another list item

> quote
> quote

"""
    print(markdown_to_html_node(md))
    print(markdown_to_html_node(md).to_html())
    
if __name__ == "__main__":
    main()