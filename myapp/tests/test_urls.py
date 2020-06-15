from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import SensorView

class TestUrls(SimpleTestCase):
    
    def test_sensor_api_url_is_resolved(self):
        url = reverse('sensor-api')
        self.assertEquals(resolve(url).func.view_class, SensorView)