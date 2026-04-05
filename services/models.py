from django.db import models

class Service(models.Model):
    TYPES = [('VISA', 'تأشيرة'), ('CITI', 'جنسية'), ('SCHO', 'منحة')]
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title
