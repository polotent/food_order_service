from django.test import TransactionTestCase
from django.core.management import call_command
from django.urls import reverse


class RestaurantsViewTest(TransactionTestCase):
    reset_sequences = True

    def test_restaurants_with_get_request(self):
        """
        If request method is not POST, an appropriate message is responsed.
        """
        response = self.client.get(reverse('orders:restaurants'))
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'error': 'Request method must be POST'}
        )

    def test_no_restaurants(self):
        """
        If no restaurants exist, an appropriate message is responsed.
        """
        response = self.client.post(reverse('orders:restaurants'))
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {'restaurants': list()}
        )

    def test_restaurants(self):
        """
        List of restaurants is reponsed.
        """
        call_command('seed')
        response = self.client.post(reverse('orders:restaurants'))
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response_json,
            {
                'restaurants': [
                    {
                        "restaurant_name": "Georgian Heaven",
                        "menu_id": 1
                    },
                    {
                        "restaurant_name": "Tasty Burgers",
                        "menu_id": 2
                    },
                    {
                        "restaurant_name": "Papa Pizza",
                        "menu_id": 3
                    },
                    {
                        "restaurant_name": "Very Hot Dog",
                        "menu_id": 4
                    },
                    {
                        "restaurant_name": "Unusual Salades",
                        "menu_id": 5
                    },
                    {
                        "restaurant_name": "Hot n Cold Coffee",
                        "menu_id": 6
                    },
                    {
                        "restaurant_name": "Chickenough",
                        "menu_id": 7
                    }
                ]
            }
        )
