from io import StringIO
from django.core.management import call_command
from django.test import TestCase


class ClosepollTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command('seed', stdout=out)
        self.assertIn('Successfully seeded initial data to db', out.getvalue())
