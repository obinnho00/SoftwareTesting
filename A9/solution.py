import unittest

# Shopping Cart System Version 1.1
cart = []

def add_item(item, price):
    """
    Adds an item with its price to the cart and returns the updated cart.
    """
    cart.append({"item": item, "price": price})
    return cart  # Return the updated cart for verification or testing

def display_cart():
    """
    Returns a list of items currently in the cart.
    """
    return [{"item": item["item"], "price": item["price"]} for item in cart]

def remove_item(item_name):
    """
    Removes an item by its name from the cart. Returns True if the item was found and removed,
    otherwise returns False.
    """
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            return True  # Indicate successful removal
    return False  # Indicate item not found

def display_total():
    """
    Calculates and returns the total price of all items in the cart.
    """
    total = sum(item["price"] for item in cart)
    return total  # Return the total for use or verification

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        # Clear the cart before each test to ensure a clean slate
        global cart
        cart = []

    def test_add_item(self):
        # Test adding a single item to the cart
        add_item("Book", 10.99)
        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]["item"], "Book")
        self.assertEqual(cart[0]["price"], 10.99)

    def test_add_multiple_items(self):
        # Test adding multiple items to the cart
        add_item("Book", 10.99)
        add_item("Pen", 1.50)
        add_item("Notebook", 5.25)
        self.assertEqual(len(cart), 3)
        self.assertEqual(cart[1]["item"], "Pen")
        self.assertEqual(cart[2]["price"], 5.25)

    def test_display_cart(self):
        # Test displaying the items in the cart
        add_item("Book", 10.99)
        add_item("Pen", 1.50)
        result = display_cart()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["item"], "Book")
        self.assertEqual(result[1]["price"], 1.50)

    def test_remove_existing_item(self):
        # Test removing an existing item from the cart
        add_item("Book", 10.99)
        add_item("Pen", 1.50)
        removed = remove_item("Pen")
        self.assertTrue(removed)
        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]["item"], "Book")

    def test_remove_non_existing_item(self):
        # Test removing an item that does not exist in the cart
        add_item("Book", 10.99)
        removed = remove_item("Laptop")
        self.assertFalse(removed)
        self.assertEqual(len(cart), 1)

    def test_display_total_price(self):
        # Test calculating the total price of items in the cart
        add_item("Book", 10.99)
        add_item("Pen", 1.50)
        add_item("Notebook", 5.25)
        total = display_total()
        self.assertAlmostEqual(total, 17.74, places=2)

    def test_display_total_price_after_removal(self):
        # Test calculating the total price after removing an item
        add_item("Book", 10.99)
        add_item("Pen", 1.50)
        add_item("Notebook", 5.25)
        remove_item("Pen")
        total = display_total()
        self.assertAlmostEqual(total, 16.24, places=2)

def main():
    unittest.main(verbosity=2)

if __name__ == "__main__":
    main()
    
