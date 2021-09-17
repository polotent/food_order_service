from django.test import TransactionTestCase
from django.core.management import call_command
from django.urls import reverse


class OrderViewTest(TransactionTestCase):
    reset_sequences = True
