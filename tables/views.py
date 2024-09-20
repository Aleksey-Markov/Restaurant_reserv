from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from tables.models import Table


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class TableReserve(ListView):
    model = Table


    # def get_object(self, queryset=None):
    #     return self.request.
