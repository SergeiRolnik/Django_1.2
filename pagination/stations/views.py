from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv

def index(request):
    return redirect(reverse('bus_stations'))

csvfile = open(BUS_STATION_CSV, encoding='utf-8', newline='')
CONTENT = list(csv.DictReader(csvfile))

def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)