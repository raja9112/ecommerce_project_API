from rest_framework import serializers
from django.contrib.auth.models import User
from decimal import Decimal

from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']
        
class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price','featured', 'category']
        
class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), default= serializers.CurrentUserDefault())
    
    def validate(self, value):
        value['price'] = value['unit_price'] * value['stock']
        return value
    
    class Meta:
        model = Cart
        fields = ['user', 'menu_item', 'stock', 'unit_price', 'price']
        extra_kwargs = {
            'price':{'read_only': True}
        }
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'menu_item', 'quantity', 'price']
        
class OrderSerializer(serializers.ModelSerializer):
    orderitem = OrderItemSerializer(many=True, read_only=True, source='order')
    
    class Meta:
        model = Order
        fields = ['id','user', 'delivery_crew', 'status', 'date', 'total', 'orderitem']
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
    
    