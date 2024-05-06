from rest_framework import serializers

from hierarchy.models import (
    Contacts,
    Products,
    Factory,
    Retail,
    Entrepreneur
)


class ContactsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для контактной информации.
    """

    class Meta:
        model = Contacts
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для товаров.
    """

    class Meta:
        model = Products
        fields = '__all__'


class FactorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для заводов.
    """

    class Meta:
        model = Factory
        fields = '__all__'


class RetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для розничной сети.
    """

    class Meta:
        model = Retail
        fields = '__all__'


class EntrepreneurSerializer(serializers.ModelSerializer):
    """
    Сериализатор для индивидуального предпринимателя.
    """

    class Meta:
        model = Entrepreneur
        fields = '__all__'

    def validate(self, attrs):
        provider_from_factory = attrs.get('provider_from_factory')
        provider_from_retailer = attrs.get('provider_from_retailer')

        if provider_from_factory and provider_from_retailer:
            raise serializers.ValidationError("Одновременно не может быть два поставщика")
        if not provider_from_factory and not provider_from_retailer:
            raise serializers.ValidationError("Хотя бы один поставщик должен быть указан")

        return attrs


class RetailUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для розничной сети.
    Запрещает обновлять поле 'debt'.
    """

    class Meta:
        model = Retail
        fields = '__all__'

    def validate(self, attrs):
        if self.instance:
            if 'debt' in attrs:
                raise serializers.ValidationError(
                    "Запрещено обновлять задолженность.")
        return attrs


class EntrepreneurUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для индивидуального предпринимателя.
    Запрещает обновлять поле 'debt'.
    """

    class Meta:
        model = Entrepreneur
        fields = '__all__'

    def validate(self, attrs):
        if self.instance:
            if 'debt' in attrs:
                raise serializers.ValidationError(
                    "Запрещено обновлять задолженность.")
        return attrs


