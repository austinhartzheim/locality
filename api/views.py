import math
from django.shortcuts import render
from django.http import JsonResponse
import osmapi


def find_nearby(request, lat, lng):
    '''
    Find points of interest near the given latitude and longitude.
    '''
    OFFSET = 0.005  # Should be a sane default

    # Cast URL parameters
    lat = float(lat)
    lng = float(lng)

    # Download nearby map data
    api = osmapi.OsmApi()
    mapdata = api.Map(lng - OFFSET, lat - OFFSET, lng + OFFSET, lat + OFFSET)

    # Select all named elements
    nearby_nodes = []
    for node in mapdata:
        if 'name' in node['data']['tag']:
            if node['type'] == 'node':
                nearby_nodes.append({
                        'lat': node['data']['lat'],
                        'lng': node['data']['lon'],
                        'tags': node['data']['tag']
                })
    
    return JsonResponse({
            'nearby_nodes': nearby_nodes
    })

