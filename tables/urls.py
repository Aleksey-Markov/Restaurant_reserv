
from django.urls import path

from tables.apps import TablesConfig
from tables.views import HomePageView, AboutView, TableReserve

app_name = TablesConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('reservation/', TableReserve.as_view(), name='reservation')
]
