from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import TenantForm


def homePage(request):
    return render(request,'index.html')
def loginPage(request):
    if request.method=="POST":
        print(request.POST.get('id_no'))
        
    return render(request,'user/login.html')
def signupPage(request):
    if request.method=="POST":
        form=TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=TenantForm()
    return render(request,'user/signup.html',{'form':form})
