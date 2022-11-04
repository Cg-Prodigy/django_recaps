from django.urls import path
from .views import landlordSignUp
urlpatterns = [
    path("sign_up/",landlordSignUp),
]
