from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    return render(request,"home.html")

def product(request):

    Mobile = int(request.GET["mobile"])
    Keyboard = int(request.GET["keyboard"])
    Monitor = int(request.GET["monitor"])
    Result = Mobile+ Keyboard+Monitor

    return render(request,"result.html",{ "result" : Result })