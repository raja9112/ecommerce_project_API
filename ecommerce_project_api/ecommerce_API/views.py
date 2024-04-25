from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

# Models
from .models import Category, MenuItem, Cart, Order, OrderItem
# Serializers
from .serializers import *

from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404

class categoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAdminUser]
            
        return [permission() for permission in permission_classes]
    
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    search_fields = ['category__title']
    ordering_fields = ['price', 'featured']
    
    def get_permissions(self):
        permission_classes= []
        if self.request.method != 'GET':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    def get_permissions(self):
        permission_classes= []
        if self.request.method != 'GET':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

# In above codes even a anon users can view categories and menu_items but here the cart will be only viewed by authenticated users - customers
# So first authenticate the user and list the cart of that particular user via get_query_set and for delete.
class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Cart.objects.all().filter(user = self.request.user)
    
    def delete(self, *args, **kwargs):
        return Cart.objects.all().filter(user = self.request.user).delete()
        return "Ok"
    