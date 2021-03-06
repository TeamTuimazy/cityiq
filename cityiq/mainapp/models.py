import requests
from bs4 import BeautifulSoup as bs
import re
import unicodedata
from pathlib import Path
import random
from .subindex10.subindex10 import Indicator46_1, Indicator46_2, Indicator47
from decimal import Decimal
from django.db import models
from django.core import serializers
from django.contrib.auth.models import User
from django.db.models import Max, Min, Count
from django.conf import settings

# функция только для тестового первичного заполнения данными БД
def wiki_info(city="Уфа"):
    def clean(i):
        a = unicodedata.normalize('NFKC', i)
        a = re.sub(r'\[\w\]', '', a)
        a = re.sub(r'\(.*?\){1,}', '', a)
        c = ('↘', '↗', 'слушать' '\n', '\t', '\r', 'произношение', ';')
        for i in c:
            a = a.replace(i, '')
        a = a.replace(' ,', ',')
        a = a.replace(' .', '.')
        a = a.replace('  ', ' ')

        return a
    def clean_population(p):
        a = unicodedata.normalize('NFKC', p)
        a = re.sub(r'\[\w\]', '', a)
        a = re.sub(r'\(.*?\){1,}', '', a)
        c = ('↘', '↗', 'слушать' '\n', '\t', '\r', 'произношение', ';')
        for i in c:
            a = a.replace(i, '')
        a = a.replace(' ,', ',')
        a = a.replace(' .', '.')
        a = a.replace('  ', ' ')

        return a

    try:
        url = f"https://ru.wikipedia.org/wiki/{city}"
        r = requests.get(url, headers={"accept-language": "ru-RU,ru"}, timeout=3)

        gerb = r.text.split('<img alt="Герб" src="')[1].split('"')[0]
        if gerb:
            gerb = f'https:{gerb}'

        soup = bs(r.text, "html.parser")
        body = soup.find(class_="mw-parser-output")
        description = body.findChildren("p", recursive=False)[0].text.strip()
        ride_side_items = body.find_all(class_="infobox-header")
        population = body.find_all('span', {'data-wikidata-property-id': 'P1082'})[0].text
        if 'городской округ' in population:
            population = population.split('городской округ')[0]
        population = int(''.join(list(map((lambda x: x if x.isdigit() else ''),clean(population)))))
        return (clean(description),
                population,
                gerb)
    except Exception as e:
        print(e)
        raise

# класс для тестового первичного наполнения БД
class First_Data_DB:
    cities = []

    def __init__(self):
        for i in range(4):
            with open(Path(settings.BASE_DIR,'city_data', str(i+1)), 'rt', encoding='utf8', errors='ignore') as fl:
                city = fl.read().split('\n')
                for c in city:
                    self.cities.append({'name':c, 'type':i+1})

    def create_cities(self):
        for city in self.cities:
            c = City()
            c.name=city.get('name')
            c.type_city=city.get('type')
            if wiki_info(city=city.get('name')):
                description, population, gerb  = wiki_info(city=city.get('name'))
                c.desc = description
                c.qty_peopls = population
                c.link_gerb = gerb
            c.save()

    def update_cities(self):
        for city in self.cities:
            c = City.objects.filter(name=city.get('name'))[0]
            if wiki_info(city=city.get('name')):
                description, population, gerb = wiki_info(city=city.get('name'))
                c.desc = description
                c.qty_peopls = population
                c.link_gerb = gerb
            c.save()

    def update_indicator_value(self):
        c = City.objects.all()
        for city in c:
            i = IndexIQ.objects.filter(city = city.id)[0]
            i461 = Indicator46_1()
            i462 = Indicator46_2()
            i47 = Indicator47()
            i.indicator46_1_value = i461.get_data(city.name)
            i.indicator46_2_value = i462.get_data(city.name)
            i.indicator47_value = i47.get_data(city.name)
            i.save()

    def update_index(self):
        c = City.objects.all()
        for city in c:
            i = IndexIQ.objects.filter(city=city.id)[0]
            i.save()

    def create_indexes(self):
        random.seed()
        cities = City.objects.all()
        for city in cities:
            ind = IndexIQ.objects.filter(city=city)
            if ind:
                index = ind[0]
            else:
                index = IndexIQ()
                index.city = city
            if index.direction1 == 0:
                index.direction1 = Decimal(random.random()*12)
            if index.direction2 == 0:
                index.direction2 = Decimal(random.random()*12)
            if index.direction3 == 0:
                index.direction3 = Decimal(random.random()*12)
            if index.direction4 == 0:
                index.direction4 = Decimal(random.random()*12)
            if index.direction5 == 0:
                index.direction5 = Decimal(random.random()*12)
            if index.direction6 == 0:
                index.direction6 = Decimal(random.random()*12)
            if index.direction7 == 0:
                index.direction7 = Decimal(random.random()*12)
            if index.direction8 == 0:
                index.direction8 = Decimal(random.random()*12)
            if index.direction9 == 0:
                index.direction9 = Decimal(random.random()*12)
            if index.direction10 == 0:
                index.direction10 = Decimal(random.random()*12)
            index.save()



class City(models.Model):
    """ Город для учета индекса IQ """
    types_city = [
        (0, 'Неизвестный'),
        (1, 'Крупнейшие города'),
        (2, 'Крупные города'),
        (3, 'Большие города'),
        (4, 'Административные центры'),
    ]

    type_city = models.IntegerField(
        default=0,
        verbose_name="Тип города",
        choices=types_city,
    )

    name = models.CharField(
        verbose_name="Название",
        max_length=100,
    )

    desc = models.TextField(
        verbose_name="Описание",
        blank=True,
    )
    qty_peopls = models.IntegerField(
        verbose_name='Население',
        default=0,
        blank=True,
    )

    link_gerb = models.CharField(
        verbose_name='Герб',
        max_length=500,
        blank=True,
    )

    def __str__(self):
        return self.name

    def get_city_type(self):
        return dict(self.types_city)[self.type_city]


    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class HistoryIndexIQ(models.Model):
    datestamp = models.DateField(
        verbose_name='Дата',
        auto_now_add=True,
    )
    serialize_object = models.TextField(
        verbose_name='Сериализованные данные',
    )

    def __str__(self):
        return "Измненеия №{} от {}".format(self.id, self.datestamp)

    class Meta:
        verbose_name = "История изменения индексов IQ"
        verbose_name_plural = "Истории изменения индексов IQ"


class IndexIQ(models.Model):
    """ Все показатели для расчета индекса iq """
    city = models.ForeignKey(
        City,
        verbose_name='Город',
        on_delete=models.CASCADE,
        related_name='city',
        unique=True,
    )

    # перечень направлений
    direction1 = models.DecimalField(
        default=Decimal("0.0"),
        verbose_name="Городское управление",
        editable=False,
        max_digits=5,
        decimal_places=2,
    )

    direction2 = models.DecimalField(
        default=Decimal("0.0"),
        verbose_name="Инновации для городской среды",
        editable=False,
        max_digits=5,
        decimal_places=2,
    )

    direction3 = models.DecimalField(
        default=Decimal("0.0"),
        verbose_name="Интеллектуальные системы общественной безопасности",
        editable=False,
        max_digits=5,
        decimal_places=2,
    )

    direction4 = models.DecimalField(
        default=Decimal("0.0"),
        verbose_name="Инфраструктура сетей связи",
        editable=False,
        max_digits=5,
        decimal_places=2,
    )

    direction5 = models.DecimalField(
        default=Decimal("0.0"),
        verbose_name="Умное ЖКХ",
        editable=False,
        max_digits=5,
        decimal_places=2,
    )

    direction6 = models.DecimalField(
        default=Decimal("0.0"),
        verbose_name="Умный городской транспорт",
        editable=False,
        max_digits=5,
        decimal_places=2,
    )

    direction7 = models.DecimalField(
        default=Decimal("0.0"),
        verbose_name="Интеллектуальные системы экологической безопасности",
        editable=False,
        max_digits=5,
        decimal_places=2,
    )

    direction8 = models.DecimalField(
        default=Decimal("0.0"),
        verbose_name="Туризм и сервис",
        editable=False,
        max_digits=5,
        decimal_places=2,
    )

    direction9 = models.DecimalField(
        default=Decimal("0.0"),
        verbose_name="Интеллектуальные системы социальных услуг",
        editable=False,
        max_digits=5,
        decimal_places=2,
    )

    direction10 = models.DecimalField(
        default=Decimal("0.0"),
        verbose_name="Экономическое состояние и инвестиционный климат",
        editable=False,
        max_digits=5,
        decimal_places=2,
    )

    # перечень индикаторов
    indicator46_1 = models.DecimalField(
        default=Decimal("0.0"),
        max_digits=5,
        decimal_places=2,
        verbose_name='Количество товаров и услуг, доступных через электронные торговые площадки на население города '
                     'по данным Yandex',
    )
    indicator46_1_value = models.DecimalField(
        default=Decimal("0.0"),
        max_digits=5,
        decimal_places=2,
        verbose_name='Данные с Yandex',
    )
    indicator46_1_date = models.DateField(
        auto_now=True,
        verbose_name='Дата получения',
    )
    indicator46_2 = models.DecimalField(
        default=Decimal("0.0"),
        max_digits=5,
        decimal_places=2,
        verbose_name='Количество товаров и услуг, доступных через электронные торговые площадки на население города '
                     'по данным Youla',
    )
    indicator46_2_value = models.DecimalField(
        default=Decimal("0.0"),
        max_digits=5,
        decimal_places=2,
        verbose_name='Данные с Youla',
    )
    indicator46_2_date = models.DateField(
        auto_now=True,
        verbose_name='Дата получения',
    )
    indicator47 = models.DecimalField(
        default=Decimal("0.0"),
        max_digits=5,
        decimal_places=2,
        verbose_name='Количество пунтков доставки компаний электронной торговли (постоматов) расположенных на '
                     'территории городских земель (2GIS)',
    )
    indicator47_value = models.IntegerField(
        default=0,
        verbose_name='Данные с 2GIS',
    )
    indicator47_date = models.DateField(
        auto_now=True,
        verbose_name='Дата получения',
    )

    index_iq = models.DecimalField(
        default=Decimal("0.0"),
        max_digits=5,
        decimal_places=2,
        editable=False,
        verbose_name='Итоговый индекс IQ',
    )

    def __str__(self):
        return "Запись индикаторов для г. {}".format(self.city)


    def max(self, indicator):
        citys_in_group = City.objects.filter(type_city=self.city.type_city).values('id')
        return IndexIQ.objects.filter(city__in=[city.get('id') for city in citys_in_group]).aggregate(
            Max(indicator)).get("{}__max".format(indicator))

    def min(self, indicator):
        citys_in_group = City.objects.filter(type_city=self.city.type_city).values('id')
        return IndexIQ.objects.filter(city__in=[city.get('id') for city in citys_in_group]).aggregate(
            Min(indicator)).get("{}__min".format(indicator))

    def update_indicators(self):
        self.indicator46_1 = round(Decimal(self.range_ind('indicator46_1_value')),2)
        self.indicator46_2 = round(Decimal(self.range_ind('indicator46_2_value')),2)
        self.indicator47 = round(Decimal(self.range_ind('indicator47_value')),2)
        self.direction10 = round((self.indicator46_1 + self.indicator46_2 + self.indicator47)/3,2)
        self.save()

    def range_ind(self, indicator, max_value_range=12):
        ind = Decimal(getattr(self, indicator))
        min = Decimal(self.min(indicator))
        max = Decimal(self.max(indicator))
        if max - min != 0:
            return (ind - min) / (max - min) * max_value_range
        else:
            return 0


    def save(self, *args, **kwargs):
        self.index_iq = self.direction1 + self.direction2 \
                        + self.direction3 +self.direction4 \
                        + self.direction5 +self.direction6 \
                        + self.direction7 + self.direction8 \
                        + self.direction9 + self.direction10
        super().save(*args, **kwargs)
        history = HistoryIndexIQ()
        history.serialize_object = serializers.serialize('json',IndexIQ.objects.filter(pk=self.id))
        history.save()


    class Meta:
        verbose_name = 'Индекс IQ'
        verbose_name_plural = 'Индексы IQ'
        get_latest_by = 'date_update'
