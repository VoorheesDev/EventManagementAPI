from apps.users.api.v1.views import CustomAuthTokenAPIView, UserCreateAPIView
from django.urls import path

urlpatterns = [
    path("signup/", UserCreateAPIView.as_view(), name="signup"),
    path("login/", CustomAuthTokenAPIView.as_view(), name="login"),
]
