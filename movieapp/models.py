from django.db import models

# Create your models here.
class Country(models.Model):
    """
     { MODELI VEERUD TULEVAD JSON FAILIST, TEHTUD PROG COUNTRIES
            "common": "French Polynesia",
            "official": "French Polynesia",
            "capital": "Papeet\u0113",
            "region": "Oceania",
            "subregion": "Polynesia",
            "flag": "https://flagcdn.com/w320/pf.png",
            "maps": "https://goo.gl/maps/xgg6BQTRyeQg4e1m6"
        }
    """
    common = models.CharField(max_length=80)
    official = models.CharField(max_length=80)
    capital = models.CharField(max_length=80)
    region = models.CharField(max_length=80)
    subregion = models.CharField(max_length=80, null=True, blank=True) # kui datas väli puudub siis on null
                                                                # kui datas väli on aga on tühi, siis on blank
    flag = models.CharField(max_length=250)
    maps = models.CharField(max_length=250)

    class Meta: # on Country alam klass
        ordering = ["common"]  # sorteerib tabeli lastname ja siis firstname järgi
        verbose_name_plural = "countries" # et nätaks mitmuses

    def __str__(self): # et ei näitaks nimesid mitte objekt 1, objekt 2 jne
        return self.common # näitab ühte veergu loetava nimega


class Movie(models.Model):
    """
    Title': 'The Walking Dead', 'Year': '2010–2022', 'imdbID': 'tt1520211', 'Type': 'series', 'Poster'
    """
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    imdbid = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    poster = models.CharField(max_length=150, null=True, blank=True)

    class Meta: # on Country alam klass
        ordering = ["title"]  # sorteerib tabeli lastname ja siis firstname järgi
        verbose_name_plural = "movies" # et nätaks mitmuses

    def __str__(self): # et ei näitaks nimesid mitte objekt 1, objekt 2 jne
        return self.title # näitab ühte veergu loetava nimega