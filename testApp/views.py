from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('HELLO')

def page_1(request):
    return HttpResponse('page_1')

def page_2(request):
    return HttpResponse('page_2')