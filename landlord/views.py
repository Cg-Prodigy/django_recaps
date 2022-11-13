from django.shortcuts import render
from .forms import LandlordSignUP
# Create your views here.

def landlordSignUp(request):
    if request.method=="POST":
        form=LandlordSignUP(request.POST)
        if form.is_valid():
            data=form.cleaned_data
    else:
        form=LandlordSignUP()
    return render(request,"landlord/signup.html",{"form":form})