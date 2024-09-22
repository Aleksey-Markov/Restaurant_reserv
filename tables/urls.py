
from django.urls import path

from tables.apps import TablesConfig
from tables.views import HomePageView, AboutView, TableReserve, TableUpdate

app_name = TablesConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('list/', TableReserve.as_view(), name='list'),
    path('reserve/<int:pk>/', TableUpdate.as_view(), name='reserve')

]
