from django.test import TestCase, Client
from django.urls import reverse
from myapp.views import SensorView
from myapp.models import Sensor
import json


# class TestSensorView(TestCase):

