from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
import requests, json, googlemaps, datetime
from .models import Pet, User
from .forms import PetForm

# Create your views here.
gmaps = googlemaps.Client(key = 'AIzaSyDWRoV2ae3J-BCp0LKXcoFdmpHxIEQnXXE')

# lost_url = 'https://data.kingcounty.gov/resource/murn-chih.json'
# lost_json= requests.get(lost_url).json()
# for item in lost_json:
#     if 'location_for_map' in item:
#         reverse_geocode_result = gmaps.reverse_geocode((item['location_for_map']['coordinates'][1],item['location_for_map']['coordinates'][0]))

def index(request):
    return render(request, 'login/index.html')

def process(request):
    if request.method == 'POST':
        if request.POST['button']==Register:
            '''register'''
            return redirect(reverse('login:main'))
        elif request.POST['button']==Login:
            '''login'''
            return redirect(reverse('login:main'))
    return redirect(reverse('login:login'))
def main(request):

    return render(request, 'login/index.html')

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
def lost(request):
    lost_url = 'https://data.kingcounty.gov/resource/murn-chih.json'
    lost_json= requests.get(lost_url).json()
    post = Pet.objects.filter(status = 'LOST')
    context = {
    'lost' : lost_json,
    'posts' : post,
    'petForm': PetForm()
    }
    return render(request, 'login/lost.html', context)
def lost_process(request):
    if request.method == 'POST':
        bound_form = petForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
        else:
            for data in bound_form.errors.itervalues():
                messages.error(request, data)
    return redirect(reverse('login:lost'))
def found(request):
    lost_url = 'https://data.kingcounty.gov/resource/murn-chih.json'
    lost_json= requests.get(lost_url).json()
    post = Pet.objects.filter(status = 'FOUND')
    form = PetForm()
    context = {
    'found' : lost_json,
    'posts' : post,
    'petForm': form
    }
    return render(request, 'login/found.html', context)
def found_process(request):
    if request.method == 'POST':
        bound_form = petForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
        else:
            for data in bound_form.errors.itervalues():
                messages.error(request, data)
    return redirect(reverse('login:found'))
