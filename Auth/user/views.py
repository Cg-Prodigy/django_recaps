from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CreateUser
def homePage(request):
    return render(request,'index.html')
def loginPage(request):
    if request.method=="POST":
        user_name=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=user_name,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.info(request,"Username or password is incorrect")
        
    return render(request,'user/login.html')
def signupPage(request):
    if request.method=="POST":
        form=CreateUser(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get("username")
            form.save()
            messages.success(request,f"Account for {user_name} has been created succesfully.")
            return redirect("login")
    else:
        form=CreateUser()
    return render(request,'user/signup.html',{'form':form})
