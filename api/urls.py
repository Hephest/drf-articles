from django.urls import path

from api import views

urlpatterns = [
    path('article/', views.ArticleList.as_view(), name='list_article'),
    path('article/<uuid:pk>/', views.ArticleDetail.as_view(), name='crud_article'),
    path('article/stats/', views.ArticleStatistics.as_view(), name='stats_article'),
    path('article/all/', views.ArticleClients.as_view(), name='clients_article'),
]