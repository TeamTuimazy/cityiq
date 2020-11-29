from django.shortcuts import render
from django.views.generic import View

from .models import City, IndexIQ

class MainView(View):
    template_name = 'mainapp/main.html'

    def get(self, request, *args, **kwargs):
        indexes = IndexIQ.objects.all().order_by('city')
        l_indexes = []
        for i, index in enumerate(indexes):
            if index.city.type_city == 1:
                if len(l_indexes) < 3:
                    l_indexes.append(index)
            elif index.city.type_city == 2:
                if len(l_indexes) < 6:
                    l_indexes.append(index)
            elif index.city.type_city == 3:
                if len(l_indexes) < 9:
                    l_indexes.append(index)
            elif index.city.type_city == 4:
                if len(l_indexes) < 12:
                    l_indexes.append(index)

        context = {
            'title': 'IQ Город',
            'index': l_indexes,
        }
        return  render(request, 'mainapp/main.html', context=context)
    def post(self):
        pass


class AllCityByTypeView(View):
    def get(self, request, type_city, *args, **kwargs):
        c = City.objects.filter(type_city=type_city)
        i = IndexIQ.objects.filter(city__in = [city.id for city in c])
        context = {
            'title': c[0].get_city_type,
            'index': i,
        }
        return  render(request, 'mainapp/allcitybytype.html', context=context)

class CityDetailView(View):
    def get(self, request, city, *args, **kwargs):
        c = City.objects.get(pk=city)
        i = IndexIQ.objects.filter(city=c)[0]
        context = {
            'title': c.name,
            'city': c,
            'index': i,
        }
        return  render(request, 'mainapp/city.html', context=context)

class RandomView(View):
    def get(self, request,  *args, **kwargs):
        c = City.objects.order_by("?").first()
        i = IndexIQ.objects.filter(city=c)[0]
        context = {
            'title': c.name,
            'city': c,
            'index': i,
        }
        return render(request, 'mainapp/city.html', context=context)

class SearchView(View):
    def post(self, request,  *args, **kwargs):
        city = request.POST['search']
        c = City.objects.filter(name__icontains=city)
        i = IndexIQ.objects.filter(city__in=[city.id for city in c])
        context = {
            'title': f"Поиск {city}",
            'city': c,
            'index': i,
            'find': city,
        }
        return render(request, 'mainapp/search.html', context=context)

class PassView(View):
    def get(self, request,  *args, **kwargs):
        context = {
            'title': f"Заглушка",
        }
        return render(request, 'mainapp/pass.html', context=context)

