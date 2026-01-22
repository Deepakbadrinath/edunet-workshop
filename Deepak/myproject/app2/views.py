from django.http import HttpResponse
from django.shortcuts import render
def login(request):
    return HttpResponse("This is the login view.")

def html_1(request):
    return render(request, 'b.html')