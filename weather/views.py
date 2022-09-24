from django.shortcuts import render
import requests
from .forms import CityForm
from .models import City


def index(request):
    appid = '84269641bb347a12d42e383af39ba401'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&&units=metric&APPID=' + appid


    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)




