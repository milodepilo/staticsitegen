import unittest

from textnode import TextNode, split_nodes_delimiter, extract_markdown_links, extract_markdown_images


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    
    def test_text_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node3 = TextNode("This is a different text node", "bold")
        self.assertNotEqual(node, node3)
    
    def test_type_not_eq(self):        
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node3 = TextNode("This is a different text node", "bold")
        node4 = TextNode("This is a different text node", "bold", "www.google.nl")
        self.assertNotEqual(node3, node4)
    
    def test_non_text_nodes(self):
        nodes = [TextNode("ignore this node", "code")]
        result = split_nodes_delimiter(nodes, '*', 'bold')  # Change 'emphasis' to 'bold'
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text_type, "code")

    def test_invalid_delimiter_use(self):
        nodes = [TextNode("some *text", "text")]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, '*', 'bold')  # Change 'emphasis' to 'bold'

    def test_proper_splitting(self):
        nodes = [TextNode("this is *important* text", "text")]
        result = split_nodes_delimiter(nodes, '*', 'bold')  # Change 'emphasis' to 'bold'
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "this is ")
        self.assertEqual(result[0].text_type, "text")
        self.assertEqual(result[1].text, "important")
        self.assertEqual(result[1].text_type, "bold")  # Text type is now 'bold'
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, "text")

    def test_extract_images(self):
        text = "This is an image: ![](http://example.com/image.png) and ![alt text](http://example.com/image2.png)"
        result = extract_markdown_images(text)
        expected = [('', 'http://example.com/image.png'), ('alt text', 'http://example.com/image2.png')]
        self.assertEqual(result, expected)

    def test_extract_links(self):
        text = "Here is a link: [](http://example.com) and [OpenAI](http://openai.com)"
        result = extract_markdown_links(text)
        expected = [('', 'http://example.com'), ('OpenAI', 'http://openai.com')]
        self.assertEqual(result, expected)

    # def test_image_and_link_together(self):
    #     text = "Check this image ![OpenAI Logo](http://openai.com/logo.png) and link [OpenAI](http://openai.com)."
    #     images = extract_markdown_images(text)
    #     links = extract_markdown_links(text)
    #     expected_images = [('OpenAI Logo', 'http://openai.com/logo.png')]
    #     expected_links = [('OpenAI', 'http://openai.com')]
    #     self.assertEqual(images, expected_images)
    #     self.assertEqual(links, expected_links)


    def test_no_matches(self):
        text = "No markdown here just text."
        images = extract_markdown_images(text)
        links = extract_markdown_links(text)
        self.assertEqual(images, [])
        self.assertEqual(links, [])


if __name__ == "__main__":
    unittest.main()
