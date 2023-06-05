import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from  pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        busstations_list = [{'Name': row['Name'], 'Street': row['Street'], 'District': row['District']} for row in reader]

    p = Paginator(busstations_list, 10)
    page = request.GET.get('page')
    page = int(page) if page else 1
    page_obj = p.get_page(page)
    page = p.page(page)
    context = {
                  'bus_stations': page_obj,
                  'page': page
    }
    return render(request, 'stations/index.html', context)
