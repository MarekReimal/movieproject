import urllib.parse
from  urllib.request import urlopen
import json
from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView) # vaated mida kasutame
from django.conf import settings
from .models import * # kõik mudelid
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView): # näitab ava lehte
    template_name = "movieapp/index.html" # movieapp/templates/index.html

class SearchView(TemplateView):
    template_name = "movieapp/search.html"

class SearchResultView(ListView):
    template_name = "movieapp/search_result.html"
    model = Country
    table = None # väärtus tuleb vormilt kas country_valik või movie_valik

    def get_queryset(self): # funkts võtab search.html vormilt sisestatud andmed
        object_list =[]
        query = self.request.GET.get("search_phrase") # vt search.html see on otsingu fraas mida kasutaja sisestab
        self.table = self.request.GET.get("choose_table") # kust tabelist otsida, kasutaja valitud vormil

        if self.table == "country_valik":
           object_list = Country.objects.filter(common__icontains=query) # object_list sisaldab vormilt saadud väärtusi
                                    # see on sql päring- kas common veerus on otsitav fraas
            #print(self.table) # prindib konsooli testiks

        elif self.table == "movie_valik":
            value = urllib.parse.quote(query) # query siin on ülevalt muutuja, rida vormindab otsingu fraasi kui seal on tühikuid
            # otsingu fraas s& on võti API poolt määratud
            search = "s=" + value
            result = "&".join([settings.OMDB_URL, search]) # result sees on url ühes tükis
            # print(result) # näita url konsoolis
            response = urlopen(result)
            data = json.loads(response.read()) # data sees on json obj
            if data["Response"] == "True":
                for obj in data["Search"]:
                    object_list.append(obj) # loop kirutab json'ist
                    # kirjutab modelisse
                    Movie.objects.get_or_create(title=obj["Title"], year=obj["Year"],
                                                imdbid=obj["imdbID"], type=obj["Type"], poster=obj["Poster"])
                    # get_or_create ei kirjuta dublikaate N kui otsid sama filmi mitu korda

        return object_list # tagastab otsingu tulemuse

    def get_context_data(self, **kwargs):  # funkts
        context = super().get_context_data(**kwargs)
        # all rida lisab object_list'i võtme choose_table ja väärtuse movie_valik või country_valik
        context["choose_table"] = self.table # vt rida  self.table = self.request.GET.get("choose_table") # kust tabelist otsida, kasutaja valitud vormil
        return context

class CountyListView(ListView):
    model = Country
    # päringud common alt sorteeritakse
    queryset = Country.objects.order_by("common")
    context_object_name = "countries"  # rida mis def muutuja et saaks for loobis kasut listi tähisena countries, muidu object_list oleks

