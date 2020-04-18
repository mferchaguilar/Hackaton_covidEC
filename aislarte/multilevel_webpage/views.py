from django.shortcuts import render

def multilevel_webpage(request):
    return render(request, 'index.html', {})
