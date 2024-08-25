from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=20, inventory=50)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream : 20")

class MenuViewTest(TestCase):
    
    def setUp(self):
        self.icecream = item = Menu.objects.create(title="IceCream", price=20, inventory=50)
        self.granola = item = Menu.objects.create(title="Granola", price=5, inventory=50)
        self.coffee = item = Menu.objects.create(title="Coffee", price=12, inventory=120)
        
    def test_getAll(self):
        self.assertEquals(self.icecream.get_item(), "IceCream : 20")
        self.assertEquals(self.granola.get_item(), "Granola : 5")
        self.assertEquals(self.coffee.get_item(), "Coffee : 12")
        
    # def test_get_item(self):
    #     item = Menu.objects.create(title="IceCream", price=20, inventory=50)
    #     self.assertEqual(item, "IceCream : 20")
        
    