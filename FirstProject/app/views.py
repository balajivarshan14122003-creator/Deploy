from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    return HttpResponse("<h1> Welcome to Django </h1>")


def index(request):
    name = ["Nainar","Sanjay","Madhu"]
    return render(request,'index.html',context={"persons":name})