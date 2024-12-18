from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


class UserModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    father_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_no = models.IntegerField()
 

class Testing(models.Model):
    test = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)


