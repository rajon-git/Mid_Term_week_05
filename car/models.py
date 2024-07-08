from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/', blank=True, null= True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)  
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE , related_name='comments')
    name = models.CharField(max_length=40)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments By {self.name}"
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    cars = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='orders', blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
