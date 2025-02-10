from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import BookAPIView, BookAPIView2, MinxinBookAPIView, BookModleViewset

router = DefaultRouter()
router.register(r'apibook5', BookModleViewset, basename='api')

urlpatterns = [
    path('', BookAPIView.as_view(), name='books'),
    path('model/', BookAPIView2.as_view(), name='books2'),
    path('mixin/', MinxinBookAPIView.as_view(), name='books3' ),
    path('', include(router.urls)),
]