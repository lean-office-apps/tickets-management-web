from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from groups.models import Group


# Create your views here.
class ListGroups(generic.ListView):
    model = Group


class CreateGroup(generic.CreateView):
    fields = ("name", "description")
    model = Group


class DeleteGroup(generic.DeleteView):
    model = Group
    success_url = reverse_lazy('list')
