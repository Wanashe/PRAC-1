from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
