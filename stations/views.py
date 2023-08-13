from django.shortcuts import render
from django.core.paginator import Paginator

import csv

from req_temp import settings

# Create your views here.


def bus_stations(request):
    page = int(request.GET.get('page', 1))

    with open(settings.BUS_STATION_CSV, 'r', encoding='utf8') as stations_csv:
        displayData = []
        reader = csv.DictReader(stations_csv)
        for row in reader:
            displayData.append({
                'name': row['Name'],
                'street': row['Street'],
                'district': row['District']
                })
            
    paginator = Paginator(displayData, 8)
    displayPage = paginator.get_page(page)
    context = {'displayPage': displayPage, 'current_page_number': page, 'last_page_number': paginator.num_pages}
    return render(request, 'stations.html', context)