from django.shortcuts import render
from django.http import HttpResponse

def aislarteweb(response):
    return render(response, 'index.html', {})
def music(request):
    return render(request, 'music.html', {})
