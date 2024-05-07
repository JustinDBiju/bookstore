from django.db import models

class Book(models.Model):
    name= models.CharField(max_length=100)
    amount=models.FloatField(max_length=200)
    desc = models.TextField(max_length=1000)
    auther = models.CharField(max_length=100,null=True)
    publisher = models.CharField(max_length=100,null=True)
    image= models.ImageField(upload_to='image')
    date = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "book"

class userModel(models.Model):
    name = models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "usertable"
