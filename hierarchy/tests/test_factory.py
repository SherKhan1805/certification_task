import pytest
from rest_framework.test import APIClient

client = APIClient()


class TestElectroFactory:
    @pytest.mark.django_db
    def test_create_factory(
            self, contact,
            product, get_bearer_token):

        url = "/hierarchy/factory/create/"

        data = {
            'name': 'test',
            'contacts': contact,
            'products': product,
        }

        response = client.post(
            url, data=data,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')
        print(response)

        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_factory_fail(
            self, contact,
            product, get_bearer_token):
        url = "/hierarchy/factory/create/"

        data = {
            'name': 'test',
            'products': product
        }

        response = client.post(
            url, data=data,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_factory(
            self,
            contact,
            product,
            factory
    ):
        url = f"/hierarchy/factory/update/{factory}/"

        data = {
            'name': 'Test1'
        }

        response = client.patch(
            url, data=data)

        assert response.status_code == 401

    @pytest.mark.django_db
    def test_get_list_factory(
            self, get_bearer_token):
        url = "/hierarchy/factory/list/?country=test"

        response = client.get(
            url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_retrieve_factory(
            self,
            factory,
            get_bearer_token
    ):
        url = f"/hierarchy/factory/{factory}/"

        response = client.get(
            url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_delete_factory(
            self,
            factory,
            get_bearer_token
    ):
        url = f"/hierarchy/factory/delete/{factory}/"

        response = client.delete(
            url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 204
