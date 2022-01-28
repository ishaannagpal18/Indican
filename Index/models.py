from django.db import models

class Details(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to="Details")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
