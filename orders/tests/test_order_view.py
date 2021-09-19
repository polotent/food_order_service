from django.test import TransactionTestCase
from django.core.management import call_command
from django.urls import reverse


class OrderViewTest(TransactionTestCase):
    reset_sequences = True

    def test_order_wrong_request_method(self):
        """
        If request method is not POST,
        an appropriate message is responsed.
        """
        response = self.client.get(
            reverse('orders:order')
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Request method must be POST'}
        )

    def test_order_without_data(self):
        """
        If request data is empty,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:order'),
            data={}
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Wrong data format'}
        )

    def test_order_without_order_id_attr(self):
        """
        If no order_id attribute in request,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:order'),
            data={
                'user_addr': 'Kazan, Lenina str, 89',
                'user_phone': '+79608765678'
            },
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Missing id parameter for order'}
        )

    def test_order_with_wrong_order_id_type(self):
        """
        If order_id attribute value type is not int,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:order'),
            data={
                'order_id': '1',
                'user_addr': 'Kazan, Lenina str, 89',
                'user_phone': '+79608765678'
            },
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Order id parameter must be int type'}
        )

    def test_order_without_user_addr_attr(self):
        """
        If no user_addr attribute in request,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:order'),
            data={
                'order_id': 1,
                'user_phone': '+79608765678'
            },
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Missing user_addr parameter for order'}
        )

    def test_order_with_wrong_user_addr_type(self):
        """
        If user_addr attribute value type is not str,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:order'),
            data={
                'order_id': 1,
                'user_addr': 89,
                'user_phone': '+79608765678'
            },
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Order user_addr parameter must be str type'}
        )

    def test_order_without_user_phone_attr(self):
        """
        If no user_phone attribute in request,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:order'),
            data={
                'order_id': 1,
                'user_addr': 'Kazan, Lenina str, 89'
            },
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Missing user_phone parameter for order'}
        )

    def test_order_with_wrong_user_phone_type(self):
        """
        If user_phone attribute value type is not str,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:order'),
            data={
                'order_id': 1,
                'user_addr': 'Kazan, Lenina str, 89',
                'user_phone': 79608765678
            },
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Order user_phone parameter must be str type'}
        )

    def test_order_with_nonexistent_order(self):
        """
        If order with given id doesn't exist,
        an appropriate message is responsed.
        """
        call_command('seed')
        response = self.client.post(
            reverse('orders:order'),
            data={
                'order_id': 1,
                'user_addr': 'Kazan, Lenina str, 89',
                'user_phone': '+79608765678'
            },
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Order not found with requested id'}
        )

    def test_order(self):
        """
        If request is correct, order status is responded.
        """
        call_command('seed')
        self.client.post(
            reverse('orders:preorder'),
            data={'items': [{'id': 1, 'quantity': 2}]},
            content_type='application/json'
        )

        response = self.client.post(
            reverse('orders:order'),
            data={
                'order_id': 1,
                'user_addr': 'Kazan, Lenina str, 89',
                'user_phone': '+79608765678'
            },
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'status': 'accepted'}
        )
