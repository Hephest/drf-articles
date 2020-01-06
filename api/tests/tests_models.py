from django.test import TestCase
from django.contrib.auth.models import User

from api.models import Article


class ArticleTest(TestCase):
    """ Test for Article Model """

    def setUp(self):
        User.objects.create_user(
            username='tester',
            password='test1234'
        )
        Article.objects.create(
            user=User.objects.get(username='tester'),
            name='Testing #1',
            created='2020-01-05',
            content='Something for test article #1'
        )
        Article.objects.create(
            user=User.objects.get(username='tester'),
            name='Testing #2',
            created='2020-01-02',
            content='TEST 2'
        )

    def test_objects_is_instances(self):
        article_1 = Article.objects.get(name='Testing #1')
        article_2 = Article.objects.get(name='Testing #2')
        self.assertIsInstance(article_1, Article)
        self.assertIsInstance(article_1, Article)

    def test_objects_count(self):
        count = Article.objects.all().count()
        self.assertEqual(count, 2)