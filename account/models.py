from django.db import models

# Create your models here.
class Custumer(models.Model):
    name = models.CharField(max_length = 150, null=True)
    phone = models.CharField(max_length = 150, null=True)
    email = models.CharField(max_length = 150, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
       return self.name




        
class Product(models.Model):
    CATEGORY = (
        ("Indor", "Indor"),
        ("Out Dor", "Out Door")
    )
    name = models.CharField(max_length = 150, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length = 150, null=True , choices=CATEGORY)
    description = models.CharField(max_length = 150, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
       return self.name
    
    
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
            ('out for delivery', 'Out for delivery'),
            ('Delivred', 'Delivred')
        )
    date_created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Custumer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length = 150, choices=STATUS)

    def __str__(self):
       return self.status
    
    