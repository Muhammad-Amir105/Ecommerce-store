from django.db import models
from decimal import Decimal

# Create your models here.
class catagory(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class brand(models.Model):
    catagory=models.ForeignKey(catagory , on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="cimg", default='')
    description=models.CharField(max_length=200)
    is_populer=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class electric_product(models.Model):
    catagory=models.ForeignKey(catagory , on_delete=models.CASCADE)
    brand=models.ForeignKey(brand , on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="cimg", blank=True)
    description=models.CharField(max_length=200)
    orignal_price=models.CharField(max_length=50)
    discount=models.IntegerField()
    quantity=models.CharField(max_length=50)
    is_populer=models.BooleanField(default=True)
    warranty=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

    def discounted_price(self):
        if self.discount is not None and int(self.discount) > 0:
            original_price_decimal = Decimal(self.orignal_price)
            discount_amount = (Decimal(self.discount) / 100) * original_price_decimal
            discounted_price = original_price_decimal - discount_amount
            return discounted_price.quantize(Decimal('0.00'))
        else:
            # If there's no discount, return the original price
            return Decimal(self.orignal_price).quantize(Decimal('0.00'))



class ProductDetail(models.Model):
    electric_product = models.ForeignKey(electric_product, on_delete=models.CASCADE)
    about_image = models.ImageField(upload_to="cimg", blank=True, null=True)
    about_title = models.CharField(max_length=50, blank=True, null=True)
    about_description = models.TextField(blank=True, null=True)
    tech_image = models.ImageField(upload_to="cimg", blank=True, null=True)
    tech_title = models.CharField(max_length=50, blank=True, null=True)
    tech_description = models.TextField(blank=True, null=True)
    camera_image = models.ImageField(upload_to="cimg", blank=True, null=True)
    camera_title = models.CharField(max_length=50, blank=True, null=True)
    camera_description = models.TextField(blank=True, null=True)
    technology_image = models.ImageField(upload_to="cimg", blank=True, null=True)
    technology_title = models.CharField(max_length=50, blank=True, null=True)
    technology_description = models.TextField(blank=True, null=True)
    design_image = models.ImageField(upload_to="cimg", blank=True, null=True)
    design_title = models.CharField(max_length=50, blank=True, null=True)
    design_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.about_title


class product_galary(models.Model):
    electproduct=models.ForeignKey(electric_product , on_delete=models.CASCADE)
    images=models.ImageField(upload_to='cimg' , blank=True , null=True)

    def __str__(self):
        return self.electproduct.name


    
class rating(models.Model):
    electproduct=models.ForeignKey(electric_product , on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    discription=models.CharField(max_length=200)
    rate=models.IntegerField(default=0)

    def __str__(self):
        return self.name



    