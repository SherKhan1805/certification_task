from rest_framework import generics

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
    EntrepreneurSerializer
)


class ContactsCreateAPIView(generics.CreateAPIView):
    """
    Создание контактной информации
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]


class ContactsListAPIView(generics.ListAPIView):
    """
    Просмотр контактной информации
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class ContactsUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение контактной информации
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class ContactsRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр контактной информации
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class ContactsDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление контактной информации
    """
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class ProductsCreateAPIView(generics.CreateAPIView):
    """
    Создание продукта
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class ProductsListAPIView(generics.ListAPIView):
    """
    Просмотр продукта
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class ProductsUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение продукта
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class ProductsRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр продукта
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class ProductsDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление продукта
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class FactoryCreateAPIView(generics.CreateAPIView):
    """
    Создание завода
    """
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class FactoryListAPIView(generics.ListAPIView):
    """
    Просмотр завода
    """
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class FactoryUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение завода
    """
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class FactoryRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр завода
    """
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class FactoryDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление завода
    """
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class RetailCreateAPIView(generics.CreateAPIView):
    """
    Создание розничной сети
    """
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class RetailListAPIView(generics.ListAPIView):
    """
    Просмотр розничной сети
    """
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class RetailUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение розничной сети
    """
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class RetailRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр розничной сети
    """
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class RetailDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление розничной сети
    """
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class EntrepreneurCreateAPIView(generics.CreateAPIView):
    """
    Создание индивидуального предпринимателя
    """
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class EntrepreneurListAPIView(generics.ListAPIView):
    """
    Просмотр индивидуального предпринимателя
    """
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class EntrepreneurUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение индивидуального предпринимателя
    """
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class EntrepreneurRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр индивидуального предпринимателя
    """
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass


class EntrepreneurDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление индивидуального предпринимателя
    """
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    # permission_classes = [IsAuthenticated, IsModer]
    pass

