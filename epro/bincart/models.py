from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class it_cart(models.Model):
    electricproduct=models.ForeignKey('main.electric_product' , on_delete=models.CASCADE)
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    date_time=models.DateTimeField(auto_now_add=True)

    def total_price(self):
        addition = self.quantity*int(self.electricproduct.orignal_price)
        return addition

    def __str__(self):
        return self.electricproduct.name