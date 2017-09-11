import random
import sys
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
        for item in self._data.get(
            'contents'
        )[0].get(
            'mainContent'
        )[1].get('records'):
            self._items.append(item.get('attributes'))

        return self._items


class DiffieHellman(object):
    @staticmethod
    def aliceInit():
        """
        return:
            A dictionary
            example:
            {
                'g': g,
                'p': p,
                'a': a,
                'A': alicePublicKey
            }

        """
        g = random.randint(100, 200)
        p = PrimeNumber().getRandomPrimeNumber(500, 100)
        a = random.randint(200, 500)
        alicePublicKey = pow(g, a, p)
        return {
            'g': g,
            'p': p,
            'a': a,
            'A': alicePublicKey
        }

    @staticmethod
    def alicekey(bobPublicKey, a, p):
        return pow(bobPublicKey, a, p)


class PrimeNumber(object):

    def isPrime(self, number):
        return all(number % integer for integer in range(2, number))

    def getRandomPrimeNumber(self, min, max):
        primes = [number for number in range(min, max) if self.isPrime(number)]
        return random.choice(primes)
