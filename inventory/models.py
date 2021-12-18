from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
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
    
class Category(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(default="Category")
    
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
    category = models.ForeignKey(
        Category,
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
        return f'{self.name}'
        
class Propertys(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    value = models.FloatField(validators=[MinValueValidator(0)],null=True,default=0)

    def __str__(self):
        return f'{self.measurement}-{self.value}'

class Request(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Approved','Approved'),        
        ('Declined','Declined'),       
        ('On hold','On hold'),       
        ('Suspended','Suspended'),  
        ('Deleted','Deleted'),      
    )
    # TYPE=(
    #     ('Purchase Request','Purchase Request'),
    #     ('Store Request','Store Request'),
    # )
    request_date = models.DateField(auto_now_add=True)
    approved_date = models.DateField(null=True)
    status = models.CharField(choices=STATUS, max_length=100, default='Pending')
    # type = models.CharField(choices=TYPE, max_length=100, default='Receive')
    request_by = models.ForeignKey(auth_models.User, on_delete=CASCADE, related_name='request_user')
    approved_by = models.ForeignKey(auth_models.User, on_delete=CASCADE, null=True, blank=True, related_name='approve_user')
    remark = models.TextField(default="for production purpuses.")

    def __str__(self):
        return f'{self.request_by}-{self.request_date}'

class RequestRow(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE,related_name="request_list")
    requested_amount = models.IntegerField(validators=[MinValueValidator(1)])
    approved_amount = models.IntegerField(validators=[MinValueValidator(0)], null=True)

    def __str__(self):
        return f'{self.item}-{self.requested_amount}'

class Purchase_Request(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Approved','Approved'),        
        ('Declined','Declined'),       
        ('On hold','On hold'),       
        ('Suspended','Suspended'),  
        ('Deleted','Deleted'),   
        ('Accepted','Accepted'),   
    )
    supplier_by = models.ForeignKey(auth_models.Supplier,on_delete=CASCADE, null=True, blank=True, related_name="supplier")
    request_date = models.DateField(auto_now_add=True)
    approved_date = models.DateField(null=True)
    status = models.CharField(choices=STATUS, max_length=100, default='Pending')
    request_by = models.ForeignKey(auth_models.User, on_delete=CASCADE, related_name='prequest_user')
    approved_by = models.ForeignKey(auth_models.User, on_delete=CASCADE, null=True, blank=True, related_name='papprove_user')
    remark = models.TextField(default="for production purpuses.")
    
    def __str__(self):
        return f'{self.supplier_by.name}-{self.request_by}-{self.request_date}'

class Purchase_Request_List(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    request = models.ForeignKey(Purchase_Request, on_delete=models.CASCADE,related_name="prequest_list")
    requested_amount = models.IntegerField(validators=[MinValueValidator(1)])
    approved_amount = models.IntegerField(validators=[MinValueValidator(0)], null=True)

    def __str__(self):
        return f'{self.item}-{self.requested_amount}'
