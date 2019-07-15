from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Bookmark
from django.views.generic.edit import *
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView


# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 3

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url','memo',]
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url','memo',]
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

