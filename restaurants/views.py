# Create your views here.

import datetime
import urllib2
import json
from django.shortcuts import render
from django.conf import settings

def index(request):
   menu = json.load(urllib2.urlopen(settings.RESTAURANTS_JSON_SRC_URL))
   for r in menu:
      r['fdate'] = datetime.datetime.fromtimestamp(r['date'])
   context = { 'menu': menu }
   return render(request, 'restaurants/index.html', context)

def formats(request):
   return render(request, 'restaurants/formats.html')
