from django.shortcuts import render
from django.http import HttpResponse, Http404 

# Create your views here.
def rules(request):
    template = 'pages/rules.html'
    return render(request, template)

def about(request):
    template = 'pages/about.html'
    return render(request, template)
