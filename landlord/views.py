from django.shortcuts import render,redirect
from .forms import LandLordForm,LandlordLogin
# Create your views here.
def landlordSignUp(request):
    if request.method=="POST":
        form=LandLordForm(request.POST)
        if form.is_valid():
            redirect(permanent=True)
    else:
        form=LandLordForm()
    return render(request,"landlord/sign_up.html",{"form":form})
def landlordLogin(request):
    if request.method=="POST":
        form=LandlordLogin(request.POST)
    else:
        form=LandlordLogin()
    return render(request,"landlord/login.html",{'form':form})