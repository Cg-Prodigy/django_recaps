from django.urls import path
from .views import loginPage,signupPage,homePage
urlpatterns = [
    path('',homePage,name='homepage'),
    path("login/",loginPage,name='login'),
    path('signup/',signupPage,name='signup')
]
