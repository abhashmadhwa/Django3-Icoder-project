from django.db import models

# Create your models here.

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=13)
    email=models.CharField(max_length=100)
    content=models.TextField()
    
    
    def __str__(self):
        return 'Message from ' +self.name
    