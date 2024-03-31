from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    Content  = models.TextField(blank=True,  null=True)
    price  = models.DecimalField(max_digits= 15, decimal_places=2, default = 99.99)
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) *0.9)
    
    def get_discount(self):
        return "122"
  
class TypeOfProduct(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()