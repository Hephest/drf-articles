from django.urls import path

from api import views

urlpatterns = [
    path('article/', views.ArticleList.as_view()),
    path('article/<uuid:pk>/', views.ArticleDetail.as_view()),
    path('article/stats/', views.ArticleStatistics.as_view()),
    path('article/all/', views.ArticleClients.as_view()),
]