from django.shortcuts import render
from .models import ScrapeData

def display_scrape_data(request):
    data = ScrapeData.objects.all() 
    return render(request, 'display_scrape_data.html', {'data': data})
