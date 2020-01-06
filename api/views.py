from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from api.models import Article
from api.serializers import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        owner = self.request.user
        return Article.objects.filter(user=owner)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        owner = self.request.user
        return Article.objects.filter(user=owner)


class ArticleStatistics(APIView):
    """
    A view that returns the count of articles in JSON.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        article_count = Article.objects.count()
        content = {
            'total': article_count
        }
        return Response(content)
