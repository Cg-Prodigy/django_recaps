from django.urls import path
from .views import landlordSignUp
urlpatterns = [
    path("signup/",landlordSignUp,name='signup')
]
