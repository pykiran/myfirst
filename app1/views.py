from django.shortcuts import render
import boto3

s3 = boto3.client("s3")

# Create your views here.
#from django.http import HttpResponse

def home(request):
    return render(request, 'new.html', {'titles': 'Home Page', 'link': 'http://youtube.com'})

def profile(request):
    return render(request, 'new.html', {'titles': 'profile page', 'link': 'http://127.0.0.1:8000/'})

def expression(request):
    a = int(request.GET['text1'])
    b = int(request.GET['text2'])
    c = a + b
    return render(request, 'output.html', {'result': c})
