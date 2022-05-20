from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def innerpage_view(request):
    return render(request, 'inner-page.html')

def PortFolio_view(request):
    return render(request, 'portfolio-details.html')