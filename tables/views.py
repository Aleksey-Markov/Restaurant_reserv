from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from tables.models import Table
from tables.services import reserve_end


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class TableReserve(ListView):
    model = Table
    queryset = Table.objects.all().order_by('pk')


class TableUpdate(UpdateView):
    reserve_end()
    model = Table
    fields = ['time_of_reserve', 'time_end_reserve', 'user_phone', 'user_name']
    success_url = reverse_lazy('tables:home')

