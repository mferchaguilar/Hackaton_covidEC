from django.shortcuts import render
from django.http import HttpResponse

def multilevel_webpage(response):
    return render(response, 'index.html', {})
