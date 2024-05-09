from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsActive

from hierarchy.models import (
    Contacts,
    Products,
    Factory,
    Retail,
    Entrepreneur
)
from hierarchy.serializers import (
    ContactsSerializer,
    ProductsSerializer,
    FactorySerializer,
    RetailSerializer,
    EntrepreneurSerializer, EntrepreneurUpdateSerializer, RetailUpdateSerializer
)


class ContactsCreateAPIView(generics.CreateAPIView):
    """
    Создание контактной информации
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ContactsListAPIView(generics.ListAPIView):
    """
    Просмотр контактной информации
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ContactsUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение контактной информации
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ContactsRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр контактной информации
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ContactsDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление контактной информации
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductsCreateAPIView(generics.CreateAPIView):
    """
    Создание продукта
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductsListAPIView(generics.ListAPIView):
    """
    Просмотр продукта
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductsUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение продукта
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductsRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр продукта
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductsDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление продукта
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class FactoryCreateAPIView(generics.CreateAPIView):
    """
    Создание завода
    """
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class FactoryListAPIView(generics.ListAPIView):
    """
    Просмотр завода
    """
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        """
        Возможность фильтрации данных по стране поставщика.
        """
        country = self.request.query_params.get('country')
        queryset = self.queryset.filter(contacts__country=country)
        return queryset


class FactoryUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение завода
    """
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class FactoryRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр завода
    """
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class FactoryDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление завода
    """
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class RetailCreateAPIView(generics.CreateAPIView):
    """
    Создание розничной сети
    """
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class RetailListAPIView(generics.ListAPIView):
    """
    Просмотр розничной сети
    """
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        """
        Возможность фильтрации данных по стране поставщика.
        """
        country = self.request.query_params.get('country')
        queryset = self.queryset.filter(contacts__country=country)
        return queryset


class RetailUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение розничной сети
    """
    serializer_class = RetailUpdateSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class RetailRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр розничной сети
    """
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class RetailDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление розничной сети
    """
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class EntrepreneurCreateAPIView(generics.CreateAPIView):
    """
    Создание индивидуального предпринимателя
    """
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class EntrepreneurListAPIView(generics.ListAPIView):
    """
    Просмотр индивидуального предпринимателя
    """
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        """
        Возможность фильтрации данных по стране поставщика.
        """
        country = self.request.query_params.get('country')
        queryset = self.queryset.filter(contacts__country=country)
        return queryset


class EntrepreneurUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение индивидуального предпринимателя
    """
    serializer_class = EntrepreneurUpdateSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class EntrepreneurRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр индивидуального предпринимателя
    """
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class EntrepreneurDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление индивидуального предпринимателя
    """
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
