from django.test import TestCase
from django.core.management import call_command
from io import StringIO


class SeedTest(TestCase):
    def test_seed_command(self):
        """
        Test seed command, which seed test data to db.
        """
        out = StringIO()
        call_command('seed', stdout=out)
        self.assertIn('Successfully seeded initial data to db', out.getvalue())
