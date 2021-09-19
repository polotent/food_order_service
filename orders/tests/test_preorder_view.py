from django.test import TransactionTestCase
from django.core.management import call_command
from django.urls import reverse


class PreorderViewTest(TransactionTestCase):
    reset_sequences = True

    def test_preorder_wrong_request_method(self):
        """
        If request method is not POST,
        an appropriate message is responsed.
        """
        response = self.client.get(
            reverse('orders:preorder'),
            data={'items': [{'id': 1, 'quantity': 2}]}
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Request method must be POST'}
        )

    def test_preorder_without_data(self):
        """
        If request data is empty,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:preorder'),
            data={}
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Wrong data format'}
        )

    def test_preorder_without_item_id_attr(self):
        """
        If no item id attribute in request,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:preorder'),
            data={'items': [{'quantity': 1}]},
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Missing id parameter for item'}
        )

    def test_preorder_with_wrong_item_id_type(self):
        """
        If item id attribute value type is not int,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:preorder'),
            data={'items': [{'id': '1'}]},
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Item id parameter must be int type'}
        )

    def test_preorder_without_item_quantity_attr(self):
        """
        If no item quantity attribute in request,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:preorder'),
            data={'items': [{'id': 1}]},
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Missing quantity parameter for item'}
        )

    def test_preorder_with_wrong_item_quantity_type(self):
        """
        If item quantity attribute value type is not int,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:preorder'),
            data={'items': [{'id': 1, 'quantity': '2'}]},
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Item quantity parameter must be int type'}
        )

    def test_preorder_with_wrong_quantity_value(self):
        """
        If item quantity attribute value is negative or 0,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:preorder'),
            data={'items': [{'id': 1, 'quantity': 0}]},
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Item quantity parameter must be positive, 0 was given'}
        )

        response = self.client.post(
            reverse('orders:preorder'),
            data={'items': [{'id': 1, 'quantity': -1}]},
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Item quantity parameter must be positive, -1 was given'}
        )

    def test_preorder(self):
        """
        If correct list of items is given,
        total_price and order_id are responded.
        """
        call_command('seed')
        response = self.client.post(
            reverse('orders:preorder'),
            data={'items': [{'id': 1, 'quantity': 2}]},
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {
                'order_id': 1,
                'total_price': 800
            }
        )

    def test_preorder_with_nonexistent_item_id(self):
        """
        If item with given id doesn't exist,
        an appropriate message is responsed.
        """
        call_command('seed')
        response = self.client.post(
            reverse('orders:preorder'),
            data={'items': [{'id': 50, 'quantity': 2}]},
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Item not found with requested id'}
        )
