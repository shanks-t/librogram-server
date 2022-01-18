from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers

from librogramapi.models import Book, Comment, UserBook, Tag, user_book, Author 
from librogramapi.serializers.book_serializer import BookSerializer

import requests
import os

class BookView(ViewSet):
    
    def create(self, request):

        user = User.objects.get(username=request.auth.user)
        book = Book.objects.get_or_create(
            title=request.data["title"],
            image_path=request.data.get("imagePath", None),
            description=request.data.get("description", None),
            page_count=request.data.get("pageCount", None),
            publisher=request.data.get("publisher", None),
            date_published=request.data.get("datePublished", None)
        )
        print(book)
        if type(book) == tuple:
            book, created = (book)
            user_book_1 = UserBook(user=user, book=book)
            user_book_1.save()
        else:
            user_book_1 = UserBook(user=user, book=book)
            user_book_1.save()
            
        authors = request.data.get('authors', None)
            
        if authors:
            for a in authors:
                obj = Author(name=a)
                obj.save()
                book.authors.add(obj)
                print(obj.name)

        request_tags = request.data.get('tags', None)

        if request_tags:
            for rt in request_tags:
                tag = Tag.objects.get_or_create(label=rt)
                tag, created = (tag)
                book.tags.add(tag)
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)
    


    def list(self, request):
        books = Book.objects.all()

        serializer = BookSerializer(
            books, many=True, context={'request': request}
        )
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, context={'request': request})
            return Response(serializer.data)

        except Book.DoesNotExist as ex:
            return Response({'message': 'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)


    @api_view
    def get_search_results(self, request):
        
        API_KEY = os.environ.get('GOOGLE_API')
        search = self.request.query_params.get('search', None)
        
        URL = f'https://www.googleapis.com/books/v1/volumes?q={search}&key={API_KEY}&maxResults=30'

        r = requests.get(url = URL)
        
        data = r.json()
        
        return Response(data)