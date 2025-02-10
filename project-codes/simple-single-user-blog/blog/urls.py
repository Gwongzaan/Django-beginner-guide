from django.urls import path
from . import views

urlpatterns = [
    path('titles/', views.titles, name='titles'), 
    path('detail/<int:id>/', views.detail, name='detail'), 
]
