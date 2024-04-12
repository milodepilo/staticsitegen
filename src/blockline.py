import block_types
from htmlnode import ParentNode, LeafNode
from textnode import text_to_textnodes, text_node_to_html



def markdown_to_blocks(md):
    blocks = md.split("\n\n")
    blocks = [block for block in blocks if block and not block.isspace()]
    return blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_types.block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_types.block_type_code  
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_types.block_type_paragraph
        return block_types.block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_types.block_type_paragraph
        return block_types.block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_types.block_type_paragraph
        return block_types.block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_types.block_type_paragraph
            i += 1
        return block_types.block_type_olist
    return block_types.block_type_paragraph

def markdown_to_html_node(md):
    parent = ParentNode("div", [])
    for block in markdown_to_blocks(md):
        # print(block)
        if block_to_block_type(block) == block_types.block_type_quote:
            parent.children.append(quote_to_html(block))
        elif block_to_block_type(block) == block_types.block_type_ulist:
            parent.children.append(ulist_to_html(block))
        elif block_to_block_type(block) == block_types.block_type_olist:
            parent.children.append(olist_to_html(block))
        elif block_to_block_type(block) == block_types.block_type_code:
            parent.children.append(code_to_html(block))
        elif block_to_block_type(block) == block_types.block_type_heading:
            parent.children.append(headings_to_html(block))
        elif block_to_block_type(block) == block_types.block_type_paragraph:
            parent.children.append(paragraph_to_html(block))
    return parent

def quote_to_html(block):
    # print(block)
    children = []
    for line in block.split("\n"):
        children.extend(text_to_children(line.lstrip("> ")))
    return ParentNode("blockquote", children)

def ulist_to_html(block):    
    html_items = []
    for line in block.split("\n"):
        children = text_to_children(line[2:])
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def olist_to_html(block):
    html_items = []
    for line in block.split("\n"):
        children = text_to_children(line[3:])
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def code_to_html(block):
    clean_code = block.replace("```", "").strip()
    html_items = []
    html_items.extend(text_to_children(clean_code))
    return ParentNode("pre", [ParentNode("code", html_items)])

def headings_to_html(block):
    # print(block)
    count = block.count("#")
    children = text_to_children(block[count:])
    return ParentNode(f"h{count}", children)

def paragraph_to_html(block):
    children = text_to_children(block)
    return ParentNode("p", children)

def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        children.append(text_node_to_html(node))
    return children
    