import unittest
from models.article import Article
from models.author import Author
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_article_creation(self):
        # Updated to use the corrected Article class
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.author_id, 1)
        self.assertEqual(article.magazine_id, 1)

    def test_magazine_creation(self):
        # Fixed by providing category argument
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    def test_author_creation(self):
        # Assuming Author is defined correctly in a similar structure
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

if __name__ == "__main__":
    unittest.main()
