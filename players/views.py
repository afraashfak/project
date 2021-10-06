from django.shortcuts import render
from django.http import HttpResponse
from .models import Players

# Create your views here.
def index(request):
    players = Players.objects.all()
    return render(request,'index.html',{'players':players})
   # return HttpResponse("<h1>Welcomeee</h1>")

def about(request):
    return HttpResponse("<h1> About the page</h1>")    