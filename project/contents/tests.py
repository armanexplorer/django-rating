import json
from users.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from .models import Content, Rating


class TestCase(APITestCase):
    list_content_url = reverse("contents:list")
    create_rate_url = reverse("contents:rate")

    def setUp(self):
        # create test users
        self.username1 = "test_user1"
        self.password1 = "test_password1"

        self.username2 = "test_user2"
        self.password2 = "test_password2"

        self.user1 = User.objects.create_user(self.username1, "test@test.com", self.password1)
        self.user2 = User.objects.create_user(self.username2, "test@test.com", self.password2)

        # create test contents
        self.title1 = 'test_title_1'
        self.text1 = 'test_desc_1'
        self.content1 = Content.objects.create(title=self.title1, text=self.text1)

        self.client.force_authenticate(self.user1)

    def test_auth(self):
        """
        Test to verify user can authenticate
        """
        response = self.client.login(username=self.username1, password=self.password1)
        self.assertTrue(response)

    def test_list_content(self):
        """
        Test to verify list content view
        """
        last_count = Content.objects.count()
        response = self.client.get(self.list_content_url)
        json_response = json.loads(response.content)
        self.assertEqual(200, response.status_code)
        self.assertTrue(len(json_response) == last_count)
        self.assertEqual(json_response[0]['title'], self.title1)

    def test_rate_create_update(self):
        """
        Test to verify creating and updating rates
        """
        # create rate
        rate_dict1 = {'user': self.user1.id, 'content': self.content1.id, 'rating': 2}
        last_count = Rating.objects.count()
        response = self.client.post(self.create_rate_url, rate_dict1)

        self.assertEqual(201, response.status_code)
        self.assertEqual(Rating.objects.count(), last_count + 1)
        self.assertEqual(Rating.objects.last().rating, 2)

        # update rate
        rate_dict2 = {'user': self.user1.id, 'content': self.content1.id, 'rating': 3}
        last_count = Rating.objects.count()
        response = self.client.post(self.create_rate_url,rate_dict2)
        self.assertEqual(201, response.status_code)  # TODO: after updating view for update, this could be 200
        self.assertEqual(Rating.objects.count(), last_count)
        self.assertEqual(Rating.objects.get(**rate_dict2).rating, 3)

    def test_avg_and_num_ratings(self):
        """
        Test to verify the average is correct
        """

        last_count = Rating.objects.count()

        # make another rate by the second user
        rate_dict =  {'user': self.user2.id, 'content': self.content1.id, 'rating': 4}
        response = self.client.post(self.create_rate_url, rate_dict)
        self.assertEqual(201, response.status_code)
        self.assertEqual(Rating.objects.count(), last_count + 1)

        rating_sum = 0
        for rating_obj in Rating.objects.all():
            rating_sum += rating_obj.rating
        avg_rating = rating_sum / Rating.objects.count()

        self.assertEqual(self.content1.rating_num, Rating.objects.count())
        self.assertEqual(self.content1.avg_rating, avg_rating)
