from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuViewTest(TestCase):
    
    @classmethod
    def setUp(self):
        self.icecream = Menu.objects.create(title="IceCream", price=20, inventory=50)
        self.granola = Menu.objects.create(title="Granola", price=5, inventory=50)
        self.coffee = Menu.objects.create(title="Coffee", price=12, inventory=120)
        
    def test_getAll(self):
        self.assertEquals(self.icecream.get_item(), "IceCream : 20")
        self.assertEquals(self.granola.get_item(), "Granola : 5")
        self.assertEquals(self.coffee.get_item(), "Coffee : 12")
        

class BookingViewTest(TestCase):

    @classmethod
    def setUp(self):
        self.testroy = Booking.objects.create(name="Test Roy", no_of_guests=1, booking_date="2024-08-25 14:30:00:00+00:00")
        self.testmarcia = Booking.objects.create(name="Test Marcia", no_of_guests=1, booking_date="2026-09-25 14:30:00:00+00:00")
        self.testalex = Booking.objects.create(name="Test Alex", no_of_guests=1, booking_date="2024-10-14 14:30:00:00+00:00")
        
    def test_getAll(self):
        self.assertEquals(self.testroy.get_item(), "Test Roy")
        self.assertEquals(self.testmarcia.get_item(), "Test Marcia")
        self.assertEquals(self.testalex.get_item(), "Test Alex")
        
    