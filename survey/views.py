  
from django.shortcuts import render,loader
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return HttpResponseRedirect('/web/')