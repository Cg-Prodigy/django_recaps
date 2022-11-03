from django.shortcuts import render
from landlord.models import House
from .forms import LoginForm
# Create your views here.
def homePage(request):
    data=House.objects.all().values() #as a dictionary
    return render(request,"home/index.html",{'data':data,})
def fomr_view(request):
    for data in request.POST:
        print("{}: {}".format(data,request.POST.getlist(data)))
    return render(request,"home/form_example.html",{"method":request.method})

def django_forms(request):
    if request.method=="POST":
        form=LoginForm(request.POST) # bound form
        if form.is_valid():
            for k,v in form.cleaned_data.items():
                print(f"{k}:[Value: {v} type: {type(v)}")
    else:
        form=LoginForm() # unbound form
    return render(request,"home/login_form.html",{'form':form})