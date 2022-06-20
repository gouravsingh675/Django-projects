from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Gourav'})

def add(request):
    val_1=int(request.POST['num1'])
    val_2=int(request.POST['num2'])
    res=val_1+val_2
    return render(request,'result.html',{'output':res})