from django.urls import path
from .views import Type1APIView, Type2APIView, Type3APIView, Type4APIView, CategoryAPIView

urlpatterns = [
    path('type1/', Type1APIView.as_view(), name='type1'), 
    path('type2/', Type1APIView.as_view(), name='type2'), 
    path('type3/', Type1APIView.as_view(), name='type3'), 
    path('type4/', Type1APIView.as_view(), name='type4'), 

    path('cat/', CategoryAPIView.as_view(), name='category' ),
]