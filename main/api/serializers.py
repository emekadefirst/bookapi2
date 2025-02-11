from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'firstname', 'lastname', 'othername', 'email', 'phone_number_1', 'phone_number_2', 'image', 'created_at']
        read_only_fields = ['id', 'created_at']