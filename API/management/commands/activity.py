# <yourapp>/management/commands/seed.py

from django.core.management.base import BaseCommand
from API.models import ActivityPeriodFactory


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--createactivity',
                            default=50,
                            type=int,
                            help='The number of fake users to create.')

    def handle(self, *args, **options):
        for _ in range(options['createactivity']):
            ActivityPeriodFactory.create()
