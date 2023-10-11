from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView,DetailView, DeleteView) # vaated mida kasutame

# Create your views here.

class HomeView(TemplateView): # näitab ava lehte
    template_name = "movieapp/index.html" # movieapp/templates/index.html