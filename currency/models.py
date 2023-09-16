from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name
