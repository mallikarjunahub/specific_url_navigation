from django.shortcuts import render

# Create your views here.
def app2_fun(request):
    return render(request, 'app2.html')