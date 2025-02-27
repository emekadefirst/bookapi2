import requests
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class GoogleLoginView(APIView):
    def post(self, request):
        access_token = request.data.get("access_token")
        if not access_token:
            return Response({"error": "Access token is required"})
        
        google_api_url = f"https://oauth2.googleapis.com/tokeninfo?id_token={access_token}"
        response = requests.get(google_api_url)
        if response.status_code != 200:
            return Response({"error": "Invalid Google token"}, status=response.status_code)
        
        user_data = response.json()
        email = user_data.get('email')
        username = user_data.get('name')
        
        user, created = User.objects.get_or_create(
            {
                "username": username,
                "email": email
            }
        )
        if created:
            user.set_unusable_password()
            user.save()
            
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                }
            }
        )