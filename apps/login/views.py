from django.shortcuts import render, redirect
from django.urls import reverse
import requests, json
import googlemaps
from datetime import datetime
# Create your views here.
gmaps = googlemaps.Client(key = 'AIzaSyDWRoV2ae3J-BCp0LKXcoFdmpHxIEQnXXE')

def index(request):
    return render(request, 'login/index.html')

def process(request):
    if request.method == 'POST':
        if request.POST['button']==Register:
            '''register'''
            return redirect(reverse('login:adopt'))
        elif request.POST['button']==Login:
            '''login'''
            return redirect(reverse('login:adopt'))
    return redirect(reverse('login:login'))

def map(request):
    buy_url = 'https://data.kingcounty.gov/resource/nu2t-d4hv.json'
    buy_json = requests.get(buy_url).json()
    lost_url = 'https://data.kingcounty.gov/resource/murn-chih.json'
    lost_json= requests.get(lost_url).json()

    context = {
        'store' : buy_json,
        'lost' : lost_json
    }
    return render(request, 'login/map.html', context)

def adopt(request):
    lost_url = 'https://data.kingcounty.gov/resource/murn-chih.json'
    lost_json= requests.get(lost_url).json()

    context = {
        'adopt' : lost_json
    }
    return render(request, 'login/adopt.html', context)
