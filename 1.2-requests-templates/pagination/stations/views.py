import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    stations_list = list()
    template_name = 'stations/index.html'
    path = settings.BUS_STATION_CSV
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            station_dict = {key: value
                            for key, value in row.items()
                            if key in ('Name', "Street", 'District')
                            }
            stations_list.append(station_dict)
    page_number = int(request.GET.get("page", 1))
    CONTENT = stations_list
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, template_name, context)
