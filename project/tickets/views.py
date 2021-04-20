from django.urls import reverse, reverse_lazy
from django.views import generic
from . import models


# Create your views here.
class TicketCreateView(generic.CreateView):
    model = models.Ticket
    fields = ('summary', 'description', 'author_name')
    success_url = reverse_lazy('tickets:list')

    # def get_success_url(self):
    #     return reverse('lawyer_detail', kwargs={'lawyer_slug': self.object.lawyer_slug})

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     # self.object.user = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)


class TicketsListView(generic.ListView):
    model = models.Ticket


class TicketDetailView(generic.DetailView):
    model = models.Ticket
