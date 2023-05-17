from django.db import models
import uuid

# Create your models here.

   
class  Product(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="Pics")
    Flipkart_Price = models.IntegerField()
    Amazon_Price = models.IntegerField() 

