from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Product(models.Model):
    """ This is the table for the products """
    product_name = models.CharField(max_length = 100)
    product_price = models.DecimalField(decimal_places = 2,max_digits = 1000,null = False)
    product_img = models.ImageField(default = 'default.png', upload_to = 'products_images')
    product_description = models.TextField(null = False,default = "This is the products description.")
    
    def save(self):
        super().save()
        
        img = Image.open(self.product_img.path)
        
        if img.width > 300 or img.height > 250:
            output_size = (300,250)
            img.thumbnail(output_size)
            img.save(self.product_img.path)
    
    def __str__(self):
        return self.product_name
    
class UserCartItems(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    item_name = models.CharField(max_length = 100)
    item_quantity = models.IntegerField(default = 1) 
    
    def __str__(self):
        return f"{self.user.username}-> {self.item_name}"
