from rest_framework.response import Response
from rest_framework import status
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.decorators import api_view

@api_view()
def main(request):
    return Response({"message": "Hello, world!", "status": status.HTTP_200_OK})
