from django.urls import path
from  . import views

app_name = "movieapp"

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"), # avaleht
    path("search/", views.SearchView.as_view(), name="search"),
    path("search_result/", views.SearchResultView.as_view(), name="search_result"),
    path("country_list/", views.CountyListView.as_view(), name="country_list"),
    path("country_detail/<int:pk>", views.CountryDetailViev.as_view(), name="country_detail"),
    path("movie_list/", views.MovieListViev.as_view(), name="movie_list"),
    path("movie_detail/<int:pk>", views.MovieDetailViev.as_view(), name="movie_detail")

]