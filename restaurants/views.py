# Create your views here.

import urllib2
import json
#from django.http import HttpResponse
from django.shortcuts import render
#from restaurants.models import Restaurant, Dish

# http://lunch.lobstertech.net/lunch/lindholmen.json

def index(request):
   menu = json.load(urllib2.urlopen('http://lunch.lobstertech.net/lunch/lindholmen.json'))
   context = {'menu': menu}
   return render(request, 'restaurants/index.html', context)
