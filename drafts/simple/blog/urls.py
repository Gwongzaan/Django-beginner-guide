from django.urls import path

from blog import views

urlpatterns = [
    path("", views.titles),
    path("<int:post_id>", views.post),
]
