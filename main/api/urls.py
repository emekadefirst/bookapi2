from .views import main, authors, get_author, create_author, delete_author
from .user.views import LoginView, SignupView, UserProfileView
from .user.google import GoogleLoginView
from django.urls import path

urlpatterns = [
    path("", main, name="Home view"),
    path("authors/", authors, name="All authors"),
    path("authors/<int:id>", get_author, name="author"),
    path("authors/create", create_author, name="Create author"),
    path("authors/delete/<int:id>", delete_author, name="Delete author"),
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("google/auth/", GoogleLoginView.as_view(), name="google auth"),
]
