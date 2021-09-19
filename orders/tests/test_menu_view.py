from django.test import TransactionTestCase
from django.core.management import call_command
from django.urls import reverse


class MenuViewTest(TransactionTestCase):
    reset_sequences = True

    def test_menu_with_get_request(self):
        """
        If request method is not POST,
        an appropriate message is responsed.
        """
        response = self.client.get(
            reverse('orders:menu'),
            data={'menu_id': 1}
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Request method must be POST'}
        )

    def test_menu_without_data(self):
        """
        If request data is empty,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:menu'),
            data={}
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Wrong data format'}
        )

    def test_menu_without_id(self):
        """
        If no id attribute in request,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:menu'),
            data={'key': 'value'},
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Missing id parameter for menu'}
        )

    def test_menu_with_wrong_id_type(self):
        """
        If id attribute value type is not int,
        an appropriate message is responsed.
        """
        response = self.client.post(
            reverse('orders:menu'),
            data={'menu_id': '2'},
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Menu menu_id parameter must be int type'}
        )

    def test_menu_with_nonexistent_menu(self):
        """
        If no menu exist, an appropriate
        message is responsed.
        """
        response = self.client.post(
            reverse('orders:menu'),
            data={'menu_id': 1},
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Menu not found with requested id'}
        )

    def test_menu(self):
        """
        List of items and menu_name are
        reponsed for specified restaurant.
        """
        call_command('seed')
        response = self.client.post(
            reverse('orders:menu'),
            data={'menu_id': 1},
            content_type='application/json'
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {
                "menu_name": "Georgian cuisine",
                "menu_items": [
                    {
                        "id": 1,
                        "item_name": "Shashlik",
                        "item_price": 400
                    },
                    {
                        "id": 2,
                        "item_name": "Potatoes",
                        "item_price": 300
                    },
                    {
                        "id": 3,
                        "item_name": "Georgian Salade",
                        "item_price": 250
                    }
                ]
            }
        )
