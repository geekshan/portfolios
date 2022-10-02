from random import choices
from django.db import models

# Create your models here.
State_Choice = ((
    ('Bihar', 'Bihar'), ('Delhi', 'Delhi'), ('UP', 'UP'), ('UK', 'UK')
))


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=State_Choice, max_length=50)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='profile_images', blank=True)
    rdoc = models.FileField(upload_to='my_doc', blank=True)
