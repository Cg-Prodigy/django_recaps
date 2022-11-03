from django.urls import path
from .views import homePage,fomr_view,django_forms
urlpatterns = [
    path('',homePage),
    path('form_example/',fomr_view),
    path('login_form/',django_forms)
]
