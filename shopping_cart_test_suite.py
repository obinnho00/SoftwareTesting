class ShoppingCart:
    def __init__(self):
        self.shopping = {"list": []}

    def add_item(self, name, price, quantity):
        found = False
        for item in self.shopping["list"]:
            if item["item"] == name:
                # Update quantity
                item["quantity"] += quantity
                # Update price to reflect the additional quantity
                item["price"] += price * quantity
                found = True
                break
        if not found:
            # Add the item as a new entry
            self.shopping["list"].append({"item": name, "price": price * quantity, "quantity": quantity})

    def remove_item(self, name, quantity=None):
        for item in self.shopping["list"]:
            if item["item"] == name:
                if quantity is None or quantity >= item["quantity"]:
                    # Remove the item entirely if no quantity is provided or if quantity is greater or equal
                    self.shopping["list"].remove(item)
                else:
                    # Reduce the quantity and update the price accordingly
                    item["quantity"] -= quantity
                    item["price"] -= (item["price"] / item["quantity"]) * quantity
                return
        raise ValueError("Item not found in the shopping cart")

    def get_price(self):
        return sum(item["price"] for item in self.shopping["list"])

    def get_item_count(self):
        return sum(item["quantity"] for item in self.shopping["list"])

    def reset(self):
        self.shopping = {"list": []}


import unittest

class Testing_shopping_cart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def tearDown(self):
        self.cart.reset()

    def test_add_item(self):
        self.cart.add_item("mango", 10, 2)
        self.assertEqual(self.cart.get_item_count(), 2)
        self.assertEqual(self.cart.get_price(), 20)

    def test_remove_item(self):
        self.cart.add_item("mango", 10, 2)
        self.cart.remove_item("mango", 2)
        self.assertEqual(self.cart.get_item_count(), 0)
        self.assertEqual(self.cart.get_price(), 0)

    def test_remove_nonExist(self):
        with self.assertRaises(ValueError):
            self.cart.remove_item("Non_existent_item", 1)

    def test_get_price(self):
        self.cart.add_item("mango", 10, 2)
        self.cart.add_item("orange", 3, 2)
        self.cart.add_item("pear", 2, 5)
        self.cart.add_item("peach", 1, 10)
        self.assertEqual(self.cart.get_price(), 46)

    def test_update(self):
        self.cart.add_item("mango", 10, 5)  
        self.cart.add_item("mango", 2, 20)  
        self.assertEqual(self.cart.get_price(), 90)  
        self.assertEqual(self.cart.get_item_count(), 25)  

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
