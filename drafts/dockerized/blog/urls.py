from django.urls import path

from blog import views

urlpatterns = [
    path('', views.title, name='title'),
    path('<int:id>/', views.posts, name='posts'),
]