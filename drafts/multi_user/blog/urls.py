from django.urls import path

from blog import views

urlpatterns = [
    path("", views.titles, name="titles"),
    path("<int:post_id>", views.post, name="post"),
]
