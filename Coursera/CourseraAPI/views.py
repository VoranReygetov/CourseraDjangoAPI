from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Book
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def books(request):
#     if request.method == 'GET':
#         books = Book.objects.all().values()
#         return JsonResponse({'books': list(books)}, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         title = request.POST.get('title')
#         author = request.POST.get('author')
#         price = request.POST.get('price')
#         inventory = request.POST.get('inventory')
#         book = Book(title = title,author = author, price = price, inventory = inventory)
#         try:
#             book.save()
#         except IntegrityError():
#             return JsonResponse({'error':'true','message':'required field missing'},status=400)
#         return JsonResponse(model_to_dict(book), status=status.HTTP_201_CREATED)
#     return Response({"message": "Unsupported request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# class BookView(APIView):
#     def get(self, request, pk):
#         return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         return Response({"title":request.data.get('title')}, status.HTTP_200_OK)


# class BookView(ViewSet):

#     def list(self, request):
#         books = Book.objects.all().values()
#         return Response({'books': list(books)}, status.HTTP_200_OK)
    
#     def create(self, request):
#         title = request.POST.get('title')
#         author = request.POST.get('author')
#         price = request.POST.get('price')
#         inventory = request.POST.get('inventory')
#         book = Book(title = title,author = author, price = price, inventory = inventory)
#         try:
#             book.save()
#         except IntegrityError():
#             return Response({'error':'true','message':'required field missing'},status=400)
#         return Response(model_to_dict(book), status=status.HTTP_201_CREATED)
    
#     def update(self, request, pk=None):
        
#         title = request.data.get('title')
#         author = request.data.get('author')
#         price = request.POST.get('price')
#         inventory = request.POST.get('inventory')
#         if pk:
#             book = Book.objects.filter(pk=pk)
#             book.update(title = title,author = author, price = price, inventory = inventory)
#             book = Book.objects.get(pk=pk)
#             return Response({"message":"Updating a book", 'book':model_to_dict(book)}, status.HTTP_200_OK)
        
#     def retrieve(self, request, pk=None):
#         if pk:
#             book = Book.objects.get(pk=pk)
#         return Response(({"message":"Displaying a book"}, model_to_dict(book)), status.HTTP_200_OK)
#     def partial_update(self, request, pk=None):
#         return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
#     def destroy(self, request, pk=None):
#         book = Book.objects.filter(pk=pk)
#         book.delete()
#         return Response({"message":"Deleting a book"}, status.HTTP_200_OK)

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SingleBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer