from http import HTTPStatus
from django.http import response

from django.test import TestCase

from cars.models import Car

class IndexViewTests(TestCase):
    def setUp(self):
        self.client.post("/login/", data={'username':'test', 'password':'testing1pass'})
    
    def test_get(self):
        response = self.client.get("/index/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<h1 class='main'>Pick your cars and see which suits you better.</h1>", html=True)
    
    def test_view_uses_correct_template(self):
        response = self.client.get("/index/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'index.html')
    
    def tearDown(self):
        self.client.get('/logout/')

class CommentFormViewTests(TestCase):
    def setUp(self):
        self.client.post("/login/", data={'username':'test', 'password':'testing1pass'})

    def test_get(self):
        response = self.client.get("/car_comments/Cayenne/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<h1>Porsche Cayenne</h1>", html=True)
        self.assertContains(response, "<h2>2 comments</h2>", html=True)
        self.assertContains(response, "<i>Average Rating: <b style='color: darkgoldenrod;'>8.5/10</b></i>", html=True)
    
    def test_success_post(self):
        response = self.client.post("/car_comments/Cayenne/", data={'name': 'Joe', 'email':'joe.winston@gmail.com', 'body':'Great car!', 'rating':7})

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<div class='alert alert-success' role='alert'>Your comment is awaiting moderation</div>", html=True)

    def test_fail_post(self):
        response = self.client.post("/car_comments/Cayenne/", data={'name': 'joe', 'email':'joewinston@gm', 'body':'Great car!', 'rating':-1})

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Should start with an uppercase letter", html=True)
        self.assertContains(response, "Enter a valid email address.", html=True)
        self.assertContains(response, "Rating should be between 1 and 10", html=True)
        
    def test_view_uses_correct_template(self):
        response = self.client.get("/car_comments/Cayenne/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'car_comments.html')