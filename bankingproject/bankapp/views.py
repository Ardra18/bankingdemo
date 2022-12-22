from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category,District


# Create your views here.
def index(request):
    return render(request,'index.html')

def allDistCat(request,c_slug=None):
    c_page=None
    districts=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        districts=District.objects.all().filter(Category=c_page,available=True)
    else:
        districts=District.objects.all().filter(available=True)
    return render(request,"category.html",{'category':c_page,'districts':districts})