from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)
    
    def __str__(self) -> str:
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index = True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(default=False, db_index=True)
    category = models.ForeignKey(Category, on_delete= models.PROTECT)
    
    def __str__(self) -> str:
        return self.title
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete= models.CASCADE)
    stock = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    
    class Meta:  # One customer should not have more than 1 same product in cart instead of they can change the stock quantity.
        unique_together = ('user', 'menu_item')
        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "delivery_crew", null= True)
    total = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    status = models.BooleanField(default=False, db_index=True)
    date = models.DateField(db_index=True)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        unique_together = ('order', 'menu_item')
        