from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from django_filters.rest_framework import DjangoFilterBackend
from api.filters import ArticleFilter

from django.contrib.auth.models import User

from api.models import Article
from api.serializers import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):
    """
    A read-write view that returns collection of articles.
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        owner = self.request.user
        return Article.objects.filter(user=owner)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A read-write-delete view for single article.
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        owner = self.request.user
        return Article.objects.filter(user=owner)


class ArticleStatistics(APIView):
    """
    A view that returns the count of articles for each user in JSON.
    """
    renderer_classes = [JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        data = []
        for each_user in User.objects.all():
            data.append({
                'user': each_user.username,
                'articles': Article.objects.filter(user=each_user).count()
            })
        return Response(data)


class ArticleClients(generics.ListAPIView):
    """
    A read-only view that shows article list to clients.
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Article.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArticleFilter
