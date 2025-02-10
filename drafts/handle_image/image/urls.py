from django.urls import path

from . import views

app_name = "image"

urlpatterns = [
    path("list-image", views.list_image, name="list_image"),
    path("upload-image", views.upload_image, name="upload_image"),
    path("del-image/", views.del_image, name="del_image"),
]
