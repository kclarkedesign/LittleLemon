from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer (serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["title", "price", "inventory"]
        
        
class BookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["name", "no_of_guests", "booking_date"]
        

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']