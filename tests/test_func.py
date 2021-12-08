from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cars.views import home_page, index_page, compare_page, choose_compare_page ,car_page
from django.test import Client


class TestFunc(SimpleTestCase):
    #test users and login 
    def test_user(self):
        c = Client()
        response = c.get('/login/', {'username': 'tester', 'password': 'testing1password1'})
        code = response.status_code
        self.assertEqual(code, 200)
        
       

