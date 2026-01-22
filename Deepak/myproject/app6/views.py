from django.http import HttpResponse
from django.shortcuts import render
def login(request):
    return HttpResponse("This is the login view.")

def html_2(request):
    return render(request, 'f.html')