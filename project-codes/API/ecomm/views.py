from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.views import APIView
from .serializer import Type1Serializer, Type2Serializer, Type3Serializer, Type4Serializer, CategorySerializer
from .models import Type1, Type2, Type3, Type4, Category

class CategoryAPIView(APIView):
    renderer_classes = [JSONRenderer, ]
    def get(self, request, format=None):
        cats = Category.objects.all()
        cat_serialixer = CategorySerializer(cats, many=True)
        return Response(cat_serialixer.data)

    def post(self, request):
        name = request.data.get('name')
        level = request.data.get('level')
        partent_cat = request.data.get('parent_cat')
        cat = Category()
        cat.name = name
        cat.level = level
        if partent_cat:
            cat.parent_cat = Category.objects.get(id=partent_cat)
        cat.save()
        cat_serializer = CategorySerializer(cat)
        return Response(cat_serializer.data)

class Type1APIView(APIView):
    renderer_classes = [JSONRenderer,]
    def get(self, request, format=None):
        types = Type1.objects.all()
        types_serializer = Type1Serializer(types, many=True)
        return Response(types_serializer.data)

class Type2APIView(APIView):
    renderer_classes = [JSONRenderer,]
    def get(self, request, format=None):
        types = Type2.objects.all()
        types_serializer = Type2Serializer(types, many=True)
        return Response(types_serializer.data)

class Type3APIView(APIView):
    renderer_classes = [JSONRenderer, ]
    def get(self, request, format=None):
        types = Type3.objects.all()
        types_serialzier = Type3Serializer(types, many=True)
        return Response(types_serialzier.data)

class Type4APIView(APIView):
    renderer_classes = [JSONRenderer, ]
    def get(self, request, format=None):
        types = Type4.objects.all()
        types_serializer = Type4Serializer(types, many=True)
        return Response(types_serializer.data)