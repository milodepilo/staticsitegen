import unittest
from blockline import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic_split(self):
        text = "First line\nSecond line\nThird line"
        result = markdown_to_blocks(text)
        expected = ["First line", "Second line", "Third line"]
        self.assertEqual(result, expected)

    def test_ignore_empty_lines(self):
        text = "First line\n\n\nSecond line\n\nThird line"
        result = markdown_to_blocks(text)
        expected = ["First line", "Second line", "Third line"]
        self.assertEqual(result, expected)

    def test_ignore_whitespace_lines(self):
        text = "First line\n   \n\t\nSecond line\n  \nThird line"
        result = markdown_to_blocks(text)
        expected = ["First line", "Second line", "Third line"]
        self.assertEqual(result, expected)

    def test_all_empty_or_whitespace(self):
        text = "\n  \n\t\n  \n"
        result = markdown_to_blocks(text)
        expected = []
        self.assertEqual(result, expected)

    def test_no_newlines(self):
        text = "Single block of text"
        result = markdown_to_blocks(text)
        expected = ["Single block of text"]
        self.assertEqual(result, expected)

    def test_trailing_newlines(self):
        text = "First line\nSecond line\n\n"
        result = markdown_to_blocks(text)
        expected = ["First line", "Second line"]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
