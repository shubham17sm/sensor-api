from django.db import models

# Create your models here.

class Sensor(models.Model):
    sname = models.CharField(max_length=40, verbose_name = 'Sensor name', null=True, blank=True)
    distance = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sname