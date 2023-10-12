import urllib, json
from urllib.request import urlopen
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movieproject.settings") # vajalik et teaks kuhu kirjutada
django.setup()
from movieapp.models import Country
# from first_app.models import Teacher

# moodul mis võtab APIst json ja kirjutab andmed mudelisse

def writeCountriesToModel(): # vaikimisi teeb viis korda, kui on argument antud siis teeb selle arvu kordi
    url = "http://restcountries.com/v3.1/all"
    response = urlopen(url)
    data = response.read()
    countries = json.loads(data)  # sisaldab listi [{riik},{riik}]

    # Country.objects.all().delete() # kustutab tabeli tühjaks kui vaja.
    # Kui on kasutusel Country.objects.get_or_create, siis delete vaja ei ole
    # get_or_create teeb tabeli tühjaks ja ei lisa dublikaate
    # vt https://stackoverflow.com/questions/4532681
    # kui kasutada Country.objects.create siis lisab modelisse dublikaadid

    for country in countries:  # country sisaldab {riik}
        if "capital" in country:  # kas võti capital on
            dcommon = country["name"]["common"]  # name on 1.level objekt ja common on name'i alamväli
            dofficial = country["name"]["official"]
            dcapital = country["capital"][0]
            dregion = country["region"]
            if "subregion" in country:
                dsubregion = country["subregion"]

            dflag = country["flags"]["png"]
            dmaps = country["maps"]["googleMaps"]
        # kirjutab andmed Modelisse
        Country.objects.get_or_create(common=dcommon, official=dofficial, capital=dcapital,
                                        region=dregion, subregion=dsubregion, flag=dflag, maps=dmaps)

writeCountriesToModel() # kutsub funkt. käivita: py .\writeCountriesToModel.py
