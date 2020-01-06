from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from django_filters.rest_framework import DjangoFilterBackend

from api.models import Article
from api.serializers import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):
    """
    A read-write view that returns collection of articles.
    """
    serializer_class = ArticleSerializer

    def get_queryset(self):
        owner = self.request.user
        return Article.objects.filter(user=owner)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A read-write-delete view for single article.
    """
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


class ArticleClients(generics.ListAPIView):
    """
    A read-only view that shows article list to clients.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'name', 'created']
