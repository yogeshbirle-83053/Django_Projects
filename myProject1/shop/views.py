from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('shop home page')

def products(request):
  return HttpResponse('shop products about page')