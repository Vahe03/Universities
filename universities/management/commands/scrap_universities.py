from itertools import count
from bs4 import BeautifulSoup
import requests

from django.core.management.base import BaseCommand

from countries.models import Country
from universities.models import University


class Command(BaseCommand):
    help = 'Scraps universities and loads into db.'

    def handle(self, *args, **options):
        universities = self.get_universities()

        for u in universities:
            c, is_created = Country.objects.get_or_create(name=u['country'])
            country_id = c.id

            u = University(
                name=u['name'],
                score=u['score'],
                rank=u['rank'],
                country=c
            )

            u.save()


    @staticmethod
    def get_universities():
        url = 'https://cwur.org/2021-22.php'
        response = requests.get(url, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'})

        response_html = response.text

        soup = BeautifulSoup(response_html, 'html.parser')

        all_data = []
        for trow in soup.select('table#cwurTable tbody tr'):
            trow = trow.contents
            all_data.append({
                'rank': trow[0].text,
                'name': trow[1].text,
                'country': trow[2].text,
                'score': trow[-1].text
            })

        return all_data
