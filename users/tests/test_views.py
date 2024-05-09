import pytest

from rest_framework import status
from rest_framework.test import APIClient

from users.models import User

client = APIClient()


@pytest.fixture
def get_bearer_token(test_user_create, test_get_token):
    """
    Тест для проверки успешного
    создания пользователя.
    """
    create_url = test_user_create
    token_url = test_get_token

    create_data = {
        'email': 'test@example.com',
        'password': 'test123456',
        'name': 'Test Name',
        'surname': 'Test Surname',
        'is_staff': True,
        'is_superuser': True,
        'is_active': True,
    }

    token_data = {
        'email': 'test@example.com',
        'password': 'test123456',
    }

    create_user = client.post(create_url, create_data)
    query_from_db = User.objects.get()
    print(query_from_db)

    get_user_token = client.post(token_url, token_data)
    print(get_user_token.data['access'])

    return get_user_token.data['access']


@pytest.fixture
def test_user_create():
    return '/user/create/'


@pytest.fixture
def test_user_list():
    return '/user/list/'


@pytest.fixture
def test_user_retrieve():
    return '/user/profile/'


@pytest.fixture
def test_user_update():
    return '/user/update/'


@pytest.fixture
def test_user_destroy():
    return '/user/delete/'


@pytest.fixture
def test_get_token():
    return '/api/token/'


@pytest.mark.django_db
def test_query_create_user(test_user_create):
    """
    Тест для проверки успешного
    создания пользователя.
    """
    url = test_user_create
    data = {
        'email': 'test@example.com',
        'password': 'test123456',
        'name': 'Test Name',
        'surname': 'Test Surname',
        'is_staff': True,
        'is_superuser': True,
    }

    response = client.post(url, data)

    query_from_db = User.objects.get()

    assert response.status_code == status.HTTP_201_CREATED

    assert data['name'] == query_from_db.name
    assert data['surname'] == query_from_db.surname
    assert data['email'] == query_from_db.email


@pytest.mark.django_db
def test_bad_request_email(test_user_create):
    """
    Тест для проверки неуспешного
    создания пользователя.
    """
    url = test_user_create
    data = {
        'password': 'test123456',
        'name': 'Test Name',
        'surname': 'Test Surname',
        'is_staff': True,
        'is_superuser': True,
    }

    response = client.post(url, data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"email": ["Обязательное поле."]}


@pytest.mark.django_db
def test_bad_request_password(test_user_create):
    """
    Тест для проверки неуспешного
    создания пользователя.
    """
    url = test_user_create
    data = {
        'email': 'test@example.com',
        'name': 'Test Name',
        'surname': 'Test Surname',
        'is_staff': True,
        'is_superuser': True,
    }

    response = client.post(url, data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"password": ["Обязательное поле."]}


@pytest.mark.django_db
def test_bad_request_name(test_user_create):
    """
    Тест для проверки неуспешного
    создания пользователя.
    """
    url = test_user_create
    data = {
        'email': 'test@example.com',
        'password': 'test123456',
        'surname': 'Test Surname',
        'is_staff': True,
        'is_superuser': True,
    }

    response = client.post(url, data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"name": ["Обязательное поле."]}


@pytest.mark.django_db
def test_bad_request_surname(test_user_create):
    """
    Тест для проверки неуспешного
    создания пользователя.
    """
    url = test_user_create
    data = {
        'email': 'test@example.com',
        'password': 'test123456',
        'name': 'Test Name',
        'is_staff': True,
        'is_superuser': True,
    }

    response = client.post(url, data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"surname": ["Обязательное поле."]}


@pytest.mark.django_db
def test_query_list(get_bearer_token, test_user_list):
    """
    Тест для проверки отображения списка
    пользователей.
    """

    list_url = test_user_list

    list_response = client.get(list_url, HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')
    print(list_response.json())

    assert list_response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_query_retrieve(get_bearer_token, test_user_retrieve):
    """
    Тест для проверки отображения определенного
    пользователя.
    """

    user_id = User.objects.get().id
    user_id_str = str(user_id)

    retrieve_url = test_user_retrieve + user_id_str + '/'

    list_response = client.get(retrieve_url, HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

    assert list_response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_query_update(get_bearer_token, test_user_update):
    """
    Тест для проверки отображения определенного
    пользователя.
    """

    user_id = User.objects.get().id
    user_id_str = str(user_id)

    data = {
        'email': 'test@example.ru',
        'password': 'test123456',
        'name': 'Test Update',
        'is_staff': True,
        'is_superuser': True,
    }

    update_url = test_user_update + user_id_str + '/'

    list_response = client.patch(update_url, data, HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')
    print(list_response.json())

    assert list_response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_query_delete(get_bearer_token, test_user_destroy):
    """
    Тест для проверки отображения определенного
    пользователя.
    """

    user_id = User.objects.get().id
    user_id_str = str(user_id)

    delete_url = test_user_destroy + user_id_str + '/'

    list_response = client.delete(delete_url, HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

    assert list_response.status_code == status.HTTP_204_NO_CONTENT
