from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0.00)
    email = models.EmailField()
    address = models.TextField(max_length=100)

    def __str__(self):
        return self.name
