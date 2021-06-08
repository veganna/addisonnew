from django.db import models

class ContactForm(models.Model):
    name                = models.CharField(max_length=60)
    email               = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

class PictureCategory(models.Model):
    p_category          = models.CharField(max_length=25, verbose_name= "Categories")

    def __str__(self):
        return self.p_category


class Picture(models.Model):
    category            = models.ForeignKey(PictureCategory, on_delete=models.CASCADE)
    title               = models.CharField(max_length=255)
    image               = models.FileField(verbose_name="Images")

class HomepageStyle(models.Model):
    style               = models.CharField(max_length=5)

    def __str__(self):
        return self.style


    
