from django.core.management.base import BaseCommand, CommandError
from django.db import connection, DatabaseError
from orders.models import Restaurant, Menu, Item
from os import path

BASE_DIR = path.dirname(path.dirname(path.dirname(path.realpath(__file__))))


class Command(BaseCommand):
    help = 'Seed database with test data'

    def clear_data(self):
        Restaurant.objects.all().delete()
        Menu.objects.all().delete()
        Item.objects.all().delete()

    def handle(self, *args, **options):
        cursor = connection.cursor()
        queries = list()
        try:
            filepath = path.join(BASE_DIR, 'seed.sql')
            with open(filepath, 'r') as f:
                queries = f.read().split(';')
        except IOError:
            raise CommandError(f'No such file \'{filepath}\'')

        try:
            self.clear_data()
        except DatabaseError as e:
            raise CommandError(f'Error during db transaction: {e}')

        for query in queries:
            if query.strip() != '':
                try:
                    cursor.execute(query)
                except DatabaseError as e:
                    raise CommandError(f'Error during db transaction: {e}')

        self.stdout.write(
            self.style.SUCCESS('Successfully seeded initial data to db')
        )
