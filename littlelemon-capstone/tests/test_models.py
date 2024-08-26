from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=20, inventory=50)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream : 20")
        

class BookingTest(TestCase):
    
    def test_get_item(self):
        reservation = Booking.objects.create(name="Test Roy", no_of_guests=1, booking_date="2024-08-25 14:30:00:00+00:00")
        reservationstr = reservation.get_item()
        self.assertEqual(reservationstr, "Test Roy")
        
        
    