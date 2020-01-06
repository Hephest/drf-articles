from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Article


class CreateReadArticleTests(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create_user('tester', 'tester@snow.com', '12345')

        Article.objects.create(
            user=User.objects.get(username='john'),
            name='Testing #1',
            created='2020-01-05',
            content='Something for test article #1'
        )
        Article.objects.create(
            user=User.objects.get(username='john'),
            name='Testing #2',
            created='2020-01-02',
            content='TEST 2'
        )
        Article.objects.create(
            user=User.objects.get(username='tester'),
            name='Testing #3',
            created='2019-12-25',
            content='3'
        )

    def test_get_articles_as_client(self):
        """
        Test clients receive all data
        """
        response = self.client.get(reverse('clients_article'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Article.objects.all().count(), 3)

    def test_get_articles_as_owner(self):
        """
        Test owner receive all data
        """
        response = self.client.get(reverse('list_article'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.all().count(), 2)
