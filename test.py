import unittest
from homework import Cart

class TestCart(unittest.TestCase):
    
    # def test_add(self):
    #     cart = Cart()
    #     cart.add()
    #     self.assertEqual(cart.grocery_dict, {'apple': {'price': 3, 'quantity': 3}})
    
    # def test_remove_it_if_not_in_the_cart_yet(self): 
    #     cart = Cart()
    #     cart.grocery_dict = {'banana': {'price': 2, 'quantity': 3}}
    #     cart.remove()
    #     self.assertEqual(cart.testvariable2, 'Item not in list')
    
    def test_remove(self): 
        cart = Cart()
        cart.grocery_dict = {'oranges': {'price': 3, 'quantity': 8}}
        cart.remove()
        self.assertEqual(cart.grocery_dict, {'oranges': {'price': 3, 'quantity': 5}})

if __name__ == '__main__':
    unittest.main()