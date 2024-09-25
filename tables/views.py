from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, UpdateView

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
    success_url = reverse_lazy('tables:list')

    def form_valid(self, form):
        table = form.save()
        user = self.request.user
        table.client = user
        table.user_phone = user.phone
        table.user_name = user.name
        table.is_reserved = True
        table.save()
        return super().form_valid(form)
