from rest_framework import serializers

from hierarchy.models import (
    Contacts,
    Products,
    Factory,
    Retail,
    Entrepreneur
)


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class FactorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Factory
        fields = '__all__'


class RetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Retail
        fields = '__all__'


class EntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = '__all__'

