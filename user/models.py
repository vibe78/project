from django.db import models
from PIL import Image
# Create your models here.
"""patients models"""
class patients(models.Model):
    Firstname = models.CharField(max_length=500)
    Othername = models.CharField(max_length=500)
    Email = models.CharField(max_length=500)
    password = models.CharField(max_length=50)
    image = models.ImageField(default='T.png', upload_to='profile_pic')

    def __str__(self):
        return self.Firstname


class Category(models.Model):
    name = models.CharField(max_length=500,null=True, blank=True, default=True)
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-time',]

    def __str__(self):
        return self.name


class category_ph(models.Model):
    name = models.CharField(max_length=500,null=True, blank=True, default=True)
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-time',]

    def __str__(self):
        return self.name
        



class Doctors(models.Model):
    Firstname = models.CharField(max_length=500)
    Othername = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    price = models.CharField(max_length=500,null=True, blank=True,)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(default='T.png', upload_to='profile_pic')
    status = models.CharField(max_length=400, default="False")


    def __str__(self):
        return self.Firstname

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size =(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)




class Pham_model(models.Model):
    First_name = models.CharField(max_length=500)
    Other_name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    #category = models.ForeignKey(category_ph, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(default='T.png', upload_to='profile_pic')


    def __str__(self):
        return self.First_name

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size =(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


'''this is the models that holds the accountant detail'''

class accountant_model(models.Model):
    First_name = models.CharField(max_length=500)
    Other_name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    #category = models.ForeignKey(category_ph, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(default='T.png', upload_to='profile_pic')


    def __str__(self):
        return self.First_name

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size =(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)




