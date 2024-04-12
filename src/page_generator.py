import os

from blockline import markdown_to_html_node
def extract_title(markdown):
    blocks = markdown.split("\n")
    if not blocks[0].startswith("# "):
        raise Exception("no title found")
    else:
        return blocks[0][2:]


def generate_page(from_path, template_path, dest_path):
    print(f"Generatinge page from{from_path}, to {dest_path}, with {template_path}")
    
    with open(from_path) as input:
        markdown = input.read()

    with open(template_path) as temp:
        template = temp.read()

    markdown_as_html = markdown_to_html_node(markdown)

    title = extract_title(markdown)

    template = template.replace('{{ Title }}', title)
    template = template.replace("{{ Content }}", markdown_as_html.to_html())

    dest_path = dest_path.replace(".md", ".html")
    print(dest_path)
    with open(dest_path, 'a') as dest:
        dest.write(template)

def generate_pages_recursively(content_dir_path, template_path, dest_dir_path):
    for item in os.listdir(content_dir_path):
        content_item = os.path.join(content_dir_path, item)
        des_item = os.path.join(dest_dir_path, item)
        if not os.path.isfile(content_item):
            generate_pages_recursively(content_item, template_path, des_item)
        else:
            generate_page(content_item, template_path, des_item)
