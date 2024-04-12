from textnode import TextNode, text_node_to_html, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_images, split_links, text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from blockline import markdown_to_blocks, block_to_block_type,markdown_to_html_node
import block_types
import os
import shutil
from page_generator import generate_page, generate_pages_recursively

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    
    generate_pages_recursively("./content", "template.html", "./public")

if __name__ == "__main__":
    main() 