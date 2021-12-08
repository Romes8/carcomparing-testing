from http import HTTPStatus

from django.test import TestCase

class CommentFormViewTests(TestCase):
    def test_get(self):
        response = self.client.get("/car_comments/Cayenne/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<h1>Porsche Cayenne</h1>", html=True)
        self.assertContains(response, "<h2>1 comments</h2>", html=True)
    
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
        
