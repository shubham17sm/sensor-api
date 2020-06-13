from django.contrib import admin

# Register your models here.
from .models import Sensor

class SensorDisplayAdmin(admin.ModelAdmin):
    list_display = ('sname', 'distance', 'date')


admin.site.register(Sensor, SensorDisplayAdmin)