from django.urls import path

from .api import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostsList.as_view(), name='posts_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]