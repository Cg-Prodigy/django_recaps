from django.urls import path
from .views import homepage,book_details
urlpatterns = [
    path('',homepage),
    path('<int:id>/',book_details)
]
