import urllib.request
import json
from django.conf import settings

class ScrapHelper(object):

   """Docstring for ScrapHelper. """
   _url = None
   _data = None
   _items = None

   def __init__(self):
       """TODO: to be defined1. """
       self._url = settings.URL_SCRAP
       self._items = []
       with urllib.request.urlopen(self._url) as url:
           self._data = json.loads(url.read().decode())

   def getItems(self):
       for item in self._data.get('contents')[0].get('mainContent')[1].get('records'):
           self._items.append(item.get('attributes'))

       return self._items
