import unittest
import logging
from datetime import datetime
import pprint as p

# Database class to store library categories, subfields, and books
class DATABASE:
    def __init__(self):
        self.Database = {
            "Fiction": {
                "Literary Fiction": [],
                "Science Fiction": [],
                "Fantasy": [],
                "Historical Fiction": [],
                "Mystery/Thriller": [],
                "Romance": [],
                "Horror": [],
                "Adventure": [],
                "Young Adult (YA)": [],
                "Dystopian": [],
                "Graphic Novels": []
            },
            "Non-Fiction": {
                "Biography/Autobiography": [],
                "Memoir": [],
                "Self-Help/Personal Development": [],
                "History": [],
                "Travel": [],
                "Science": [],
                "Philosophy": [],
                "Business/Finance": [],
                "Politics": [],
                "Religion/Spirituality": [],
                "True Crime": [],
                "Education/Academic": []
            },
        }

# Library management system to add, search, and remove books
class LibraryManagementSystem:
    def __init__(self, database):
        self.database = database

    # Adds a book to the specified category and subfield
    def add_book(self, category, subfield, book_name, author):
        normalized_category = self._get_normalized_key(category, self.database.Database)
        if normalized_category is None:
            logging.error(f"Category '{category}' not found.")
            return
        
        normalized_subfield = self._get_normalized_key(subfield, self.database.Database[normalized_category])
        if normalized_subfield is None:
            logging.error(f"Subfield '{subfield}' not found in category '{category}'.")
            return

        entry = {
            "ID": str(datetime.now().timestamp()).replace(".", ""),
            "Book Name": book_name,
            "Author": author,
            "Date Added": str(datetime.now().timestamp()).replace(".", "")
        }
        
        self.database.Database[normalized_category][normalized_subfield].append(entry)
        logging.info(f"Book '{book_name}' added to {subfield} in {category}.")

    # Searches for a book by name in the specified category
    def search_book(self, category, book):
        normalized_category = self._get_normalized_key(category, self.database.Database)
        if normalized_category is None:
            logging.error(f"Category '{category}' not found.")
            return
        
        for subcategory, books in self.database.Database[normalized_category].items():
            for items in books:
                if items["Book Name"].lower() == book.lower():
                    logging.info(f"'{book}' found in '{subcategory}' under '{category}'")
                    return
        logging.error(f"'{book}' not found in any subcategory under '{category}'")

    # Removes a book from the specified category and subfield
    def remove_book(self, category, book_name):
        normalized_category = self._get_normalized_key(category, self.database.Database)
        if normalized_category is None:
            logging.error("Category Not found in book database")
            return 
    
        for subcategory, books in self.database.Database[normalized_category].items():
            for data in books:
                if data["Book Name"].lower() == book_name.lower():
                    books.pop(books.index(data))
                    logging.info(f"'{book_name.title()}' and all associated data removed from '{subcategory}' under '{category}'")
                    return
         
        logging.error(f"'{book_name.title()}' not found in any subcategory under '{category}'")

    # Normalizes the input key to match the dictionary key (case-insensitive)
    def _get_normalized_key(self, input_key, dictionary):
        for key in dictionary:
            if key.lower() == input_key.lower():
                return key
        return None

# Unit tests for the library management system
class TestLibraryManagementSystem(unittest.TestCase):
    
    def setUp(self):
        """Sets up the library management system and database for each test."""
        self.db = DATABASE()
        self.library = LibraryManagementSystem(self.db)

    # Tests adding a valid book to a valid category and subfield
    def test_add_valid_book(self):
        self.library.add_book("Fiction", "Science Fiction", "Dune", "Frank Herbert")
        books = self.db.Database["Fiction"]["Science Fiction"]
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["Book Name"], "Dune")
        self.assertEqual(books[0]["Author"], "Frank Herbert")
    
    # Tests adding a book to an invalid category
    def test_add_invalid_category(self):
        with self.assertLogs() as log:
            self.library.add_book("InvalidCategory", "Science Fiction", "Dune", "Frank Herbert")
            self.assertIn("Category 'InvalidCategory' not found.", log.output[0])
    
    # Tests adding a book to an invalid subfield
    def test_add_invalid_subfield(self):
        with self.assertLogs() as log:
            self.library.add_book("Fiction", "InvalidSubfield", "Dune", "Frank Herbert")
            self.assertIn("Subfield 'InvalidSubfield' not found in category 'Fiction'.", log.output[0])
    
    # Tests searching for a book that exists
    def test_search_book_found(self):
        self.library.add_book("Fiction", "Science Fiction", "Dune", "Frank Herbert")
        with self.assertLogs() as log:
            self.library.search_book("Fiction", "Dune")
            self.assertIn("'Dune' found in 'Science Fiction' under 'Fiction'", log.output[0])
    
    # Tests searching for a book that doesn't exist
    def test_search_book_not_found(self):
        with self.assertLogs() as log:
            self.library.search_book("Fiction", "Nonexistent Book")
            self.assertIn("'Nonexistent Book' not found in any subcategory under 'Fiction'", log.output[0])
    
    # Tests removing a book that exists
    def test_remove_book(self):
        self.library.add_book("Fiction", "Science Fiction", "Dune", "Frank Herbert")
        self.library.remove_book("Fiction", "Dune")
        books = self.db.Database["Fiction"]["Science Fiction"]
        self.assertEqual(len(books), 0)

    # Tests removing a book that doesn't exist
    def test_remove_nonexistent_book(self):
        with self.assertLogs() as log:
            self.library.remove_book("Fiction", "Nonexistent Book")
            self.assertIn("'Nonexistent Book' not found in any subcategory under 'Fiction'", log.output[0])

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
