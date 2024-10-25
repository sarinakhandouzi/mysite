from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return render(request , 'mysite/templates/website/index.html')

def about_view(request):
    return render(request , 'mysite/templates/website/about.html')

def contact_view(request):
    return render(request , 'mysite/templates/website/contact.html')