from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
import urllib
from django.utils import timezone


def home(request):
     if request.method =='POST':
          city = request.POST['city']
          city.replace(" ", "")

          if city=="":
               city="Delhi"
     else:
          city="Delhi"

     source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=3ba0594ae8623b6ffbfff2d0de8d5969').read()
          
     data_list=json.loads(source)
     lon=str(data_list['coord']['lon'])
     lat=str(data_list['coord']['lat'])
     print(lat,lon)
     data={
               "city":city,
               "country_code":str(data_list['sys']['country']),
               "temp":str(round(data_list['main']['temp']-273,1)) + '°C',
               "pressure":str(data_list['main']['pressure']),
               "max":str(round(data_list['main']['temp_max']-273,1)) + '°C',
               "min":str(round(data_list['main']['temp_min']-273,1)) + '°C', #temp_min
               "humidity":str(data_list['wind']['speed']),
               "visibility":str(data_list['visibility']),
               "main":str(data_list['weather'][0]['main']),
               "description":str(data_list['weather'][0]['description']),
               "icon":str(data_list['weather'][0]['icon']),
               "date":timezone.now().date(),
     }
     print(data)
          
          
     exclude = 'minute,hourly'
     source2=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lon+'&exclude=minute,hourly&appid=3ba0594ae8623b6ffbfff2d0de8d5969').read()
     data_list2=json.loads(source2)
     print(data_list2)
     for i in data_list2['daily']:
               print(i['temp']['day'])
               print(i['weather'][0]['description'])
          
          #data2={
           #    "temperature":str(data_list2['temp'][0]['day']),
            #   }
          #print(data2)
          #print(data_list2)
     
          
     return render(request, 'home.html', data)
