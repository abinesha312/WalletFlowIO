from django.urls import path
from .views import UserRegistrationView, CustomAuthToken

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    # A settings endpoint can be added here if desired.
]
