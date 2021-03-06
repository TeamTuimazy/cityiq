from django.urls import path, include
from .views import MainView, AllCityByTypeView, CityDetailView, RandomView, SearchView, PassView, SubindexDetail, AboutView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('tcity/<int:type_city>/', AllCityByTypeView.as_view(), name='city_type'),
    path('city/<int:city>/', CityDetailView.as_view(), name='city'),
    path('random/', RandomView.as_view(), name='random'),
    path('search/', SearchView.as_view(), name='search'),
    path('pass/', PassView.as_view(), name='pass'),
    path('about/', AboutView.as_view(), name='about'),
    path('subindex/<int:city>/<int:subindex_id>', SubindexDetail.as_view(), name='subindex'),
]

