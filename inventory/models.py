from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE
from authentications import models as auth_models
# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    max_capacity = models.IntegerField(validators=[MinValueValidator(0)])
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(auth_models.User, on_delete=CASCADE)

    def __str__(self):
        return f'{ self.name }-{ self.location }'

class Shelf(models.Model):
    name = models.CharField(max_length=500)
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE
    )
    max_capacity = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(default="Shalf for items.")
    
    def __str__(self):
        return f'{ self.store.name }-{ self.name }'
    
class Catagory(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(default="Catagory")
    
    def __str__(self):
        return self.name

class Measurement(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(default="Measurement")
    
    def __str__(self):
        return self.name

class Items(models.Model):
    name = models.CharField(max_length=500)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    color = models.CharField(max_length=100, null=True)
    # hight width thickness 
    catagory = models.ForeignKey(
        Catagory,
        models.SET_NULL,
        blank=True,
        null=True
    )
    cost = models.FloatField(validators=[MinValueValidator(0)],null=True,default=0)
    image = models.ImageField(upload_to="inventory/image/",null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(default="Measurement")
    
    def __str__(self):
        return f'{self.name}-size{self.width}*{self.hight}'


class Propertys(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    value = models.FloatField(validators=[MinValueValidator(0)],null=True,default=0)

    def __str__(self):
        return f'{self.measurement}-{self.value}'
        