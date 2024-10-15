from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return str(self.friendly_name)


class Brand(models.Model):
    brand = models.CharField(max_length=20, null=False, default="")
    support_page = models.CharField(max_length=254, null=False, default="")
    
    def __str__(self):
        return str(self.brand)


class Tag(models.Model):
    tag = models.CharField(max_length=10, null=False, default="")
    friendly_tag = models.CharField(max_length=16, null=False, default="")
    
    def __str__(self):
        return str(self.tag)
    
    def get_friendly_tag(self):
        return str(self.friendly_tag)


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL
    )
    tags = models.ManyToManyField(Tag)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)