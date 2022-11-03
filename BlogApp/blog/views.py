from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def homepage(request):
    data=Post.pp.all()
    print(data)
    return render(request,'index.html',{'post':data})

def book_details(request,id):
    data=get_object_or_404(Post,id=id)
    return render(request,'details.html',{'data':data})