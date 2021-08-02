from django.db import models


class SupplyCategory(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class SupplyItem(models.Model):
    name = models.CharField(max_length=120)
    picture = models.FileField()
    description = models.TextField()
    category = models.ForeignKey(SupplyCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
