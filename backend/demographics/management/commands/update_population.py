from django.core.management.base import BaseCommand
from demographics.tasks import fetch_and_update_population

class Command(BaseCommand):
    help = 'Fetch and update population data manually'
    
    def handle(self, *args, **kwargs):
        fetch_and_update_population()