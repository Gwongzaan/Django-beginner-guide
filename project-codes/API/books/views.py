from django.shortcuts import render
from .serializers import BookSerializer , BookModelSerializer
from .models import Book
from users.models import UserProfile
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.permissions import BasePermission 

class BookAPIView(APIView):
    def get(self, request, format=None):
        APIKey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            if developer.balance> 0 :
                isbn = self.request.query_params.get('isbn', 0)
                books = Book.objects.filter(isbn=isbn)
                books_serializer = BookSerializer(books, many=True)
                developer.balance -= 1
                developer.save()
                return Response(books_serializer.data)
            else:
                return Response('low balance')

        else:
            return Response('unauthorized')

class BookAPIView2(APIView):
    def get(self, request, format=None):
        APIkey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIkey).first()
        if developer:
            if developer.balance > 0:
                isbn = self.request.query_params.get('isbn', 0)
                books = Book.objects.filter(isbn=isbn)
                books_serialzier = BookModelSerializer(books, many=True)
                developer.balance -=1 
                developer.save()
                return Response(books_serialzier.data)

            else:
                return Response('low balance')

        else:
            return Response('unauthorized')

class MinxinBookAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    
    def get(self, request, *args, **kwargs):
        APIkey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIkey).first() 
        if developer:
            if developer.balance > 0:
                isbn = self.request.query_params.get('isbn', 0)
                developer.balance -= 1
                developer.save()
                self.queryset = Book.objects.filter(isbn=isbn)
                return self.list(request, *args, **kwargs)
            else:
                return Response("low balance")

        return Response('unauthorized')


# the only difference here is that the mixin abover required to define get()
class MinxinBookAPIView2(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    
    def get(self, request, *args, **kwargs):
        APIkey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIkey).first() 
        if developer:
            if developer.balance > 0:
                isbn = self.request.query_params.get('isbn', 0)
                developer.balance -= 1
                developer.save()
                self.queryset = Book.objects.filter(isbn=isbn)
                return self.list(request, *args, **kwargs)
            else:
                return Response("low balance")

        return Response('unauthorized')

class IsDeveloper(BasePermission):
    message = "unauthorized"
    def has_permission(self, request, view):
        APIkey = request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIkey).first()
        if developer:
            return True
        else:
            print(self.message)
            return False

class EnoughBalance(BasePermission):
    message = "low balance"
    def has_permission(self, request, view):
        APIkey = request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIkey).first()
        if developer.balance > 0:
            developer.balance -= 1
            developer.save()
            return True

        else:
            return False


class BookModleViewset(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = [IsDeveloper, EnoughBalance, ]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get_queryset(self):
        isbn = self.request.query_params.get('isbn', 0)
        books = Book.objects.filter(isbn=isbn)
        queryset=books
        return queryset