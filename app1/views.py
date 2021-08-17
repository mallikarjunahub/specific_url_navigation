from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_fun(request):
    return render(request, 'app1.html')
    
def app1_string(request):
    return HttpResponse('<h1>this is app1 string content')