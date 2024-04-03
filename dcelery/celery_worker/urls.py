from django.urls import path
from .views import display_scrape_data

urlpatterns = [
    path('', display_scrape_data, name='display_scrape_data'),
]