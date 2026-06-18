from django.urls import path

from .views import UserListCreateView, UserDetailView, UserLoginView

urlpatterns = [
    path("users/", UserListCreateView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
    path("users/login/", UserLoginView.as_view()),
]
