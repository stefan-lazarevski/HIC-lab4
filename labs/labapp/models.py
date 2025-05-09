from django.db import models

# Create your models here.

class Suplement(models.Model):
    kategorija = [
        ('proteins', 'proteins'),
        ('vitamins', 'vitamins'),
        ('creatines', 'creatines'),
        ('amino acids', 'amino acids'),
        ('pre-workout', 'pre-workout')
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="item_photos/", null=True, blank=True)
    code = models.CharField(max_length=100, unique=True)
    manufacturer = models.CharField(max_length=100)
    available = models.BooleanField(default=False)
    price = models.IntegerField()
    category = models.CharField(max_length=30, choices=kategorija)

    def __str__(self):
        return f'{self.name}'