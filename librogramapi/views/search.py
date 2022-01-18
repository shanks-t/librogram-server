from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
import requests


@api_view(['GET'])
def search_results(request):
        API_KEY = os.environ.get('GOOGLE_API')
        search = request.query_params.get('q', None)
        
        URL = f'https://www.googleapis.com/books/v1/volumes?q={search}&key={API_KEY}&maxResults=30'

        r = requests.get(url = URL)
        
        data = r.json()
        
        return Response(data)