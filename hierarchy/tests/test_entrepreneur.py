import pytest
from rest_framework.test import APIClient

client = APIClient()


class TestRetail:
    @pytest.mark.django_db
    def test_create_trader(
            self, contact,
            product, factory,
            get_bearer_token
    ):
        url = "/hierarchy/entrepreneur/create/"

        data = {
            'name': 'test',
            'contacts': contact,
            'products': product,
            'provider_from_factory': factory,
            'debt': 10000.00
        }

        response = client.post(
            url, data=data,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_trader_fail(
            self, contact,
            product, get_bearer_token
    ):
        url = "/hierarchy/entrepreneur/create/"

        data = {
            'name': 'test',
            'products': product,
            'contacts': contact,

            'debt': 10000.00

        }

        response = client.post(
            url, data=data,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_trader(
            self,
            trader,
            get_bearer_token
    ):
        url = f"/hierarchy/entrepreneur/update/{trader}/"

        data = {
            'name': 'Test1'
        }

        response = client.patch(
            url, data=data,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}'
        )

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_update_trader_fail(
            self,
            retail,
            get_bearer_token
    ):
        url = f"/hierarchy/entrepreneur/update/{retail}/"

        data = {
            'debt': 2000.00
        }

        response = client.patch(
            url, data=data,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}'
        )

        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_list_trader(
            self, get_bearer_token):
        url = "/hierarchy/entrepreneur/list/?country=test"

        response = client.get(
            url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_retrieve_trader(
            self,
            trader,
            get_bearer_token
    ):
        url = f"/hierarchy/entrepreneur/{trader}/"

        response = client.get(
            url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_delete_trader(
            self,
            trader,
            get_bearer_token
    ):
        url = f"/hierarchy/entrepreneur/delete/{trader}/"

        response = client.delete(
            url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 204

