from htmlnode import HTMLNode, LeafNode, ParentNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(tag='p', value='Hello, world!', props={'id': 'intro', 'class': 'highlight'})
        self.assertEqual(node1.props_to_html(), ' id="intro" class="highlight"')

    def test_no_properties(self):
        node = HTMLNode(tag='div')
        self.assertEqual(node.props_to_html(), '')

    def test_single_property(self):
        node = HTMLNode(tag='div', props={'id': 'main'})
        self.assertEqual(node.props_to_html(), ' id="main"')

    def test_multiple_properties(self):
        node = HTMLNode(tag='div', props={'id': 'main', 'class': 'container'})
        self.assertTrue(' id="main"' in node.props_to_html() and ' class="container"' in node.props_to_html())
        self.assertEqual(len(node.props_to_html().strip().split(' ')), 2)  # Ensuring exactly two properties

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [HTMLNode(tag='p', value='test')])
            node.to_html()

    def test_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode('div', None)
            node.to_html()

    def test_simple_html_generation(self):
        child1 = LeafNode(tag='p', value='Hello')
        child2 = LeafNode(tag='p', value='World')
        parent = ParentNode('div', [child1, child2])
        self.assertEqual(parent.to_html(), '<div><p>Hello</p><p>World</p></div>')

    def test_nested_structure(self):
        grandchild = LeafNode(tag='span', value='Click here')
        child = ParentNode('button', [grandchild], {'type': 'button'})
        parent = ParentNode('div', [child])
        expected_html = '<div><button type="button"><span>Click here</span></button></div>'
        self.assertEqual(parent.to_html(), expected_html)