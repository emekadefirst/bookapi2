from .views import main
from django.urls import path

urlpatterns = [
    path('', main, name="Home view"),
]
