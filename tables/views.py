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

    def setup(self, request, *args, **kwargs):
        reserve_end()
        super().setup(request, *args, **kwargs)


class TableUpdate(UpdateView):
    model = Table
    fields = ['time_of_reserve', 'time_end_reserve', 'user_phone', 'user_name']
    success_url = reverse_lazy('tables:home')

    def post(self, request, *args, **kwargs):
        table = self.get_object()
        table.client = request.user
        table.user_phone = request.user.phone
        table.user_name = request.user.name
        table.is_reserved = True
        table.save()
        return super().post(request, *args, **kwargs)

