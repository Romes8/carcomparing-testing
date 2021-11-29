from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cars.views import home_page, index_page

class TestUrls(SimpleTestCase):
    def test_inedx_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index_page)
        
    


        