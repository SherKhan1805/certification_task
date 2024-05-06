from rest_framework import serializers


class HierarchyCustomValidator:
    """
    Валидатор для выбора поставщика
    """

    def __init__(self, name,
                 provider_from_factory,
                 provider_from_retailer):
        self.name = name
        self.provider_from_factory = provider_from_factory
        self.provider_from_retailer = provider_from_retailer

    def __call__(self, value):
        name = value.get(self.name)
        provider_from_factory = value.get(self.provider_from_factory)
        provider_from_retailer = value.get(self.provider_from_retailer)

        if name is not None:
            # проверка создания поставщика
            if provider_from_factory is not None and provider_from_retailer is not None:
                raise serializers.ValidationError(
                    'У продукта не может быть одновременно поставщиков с завода и розничной сети')
            if provider_from_factory is None and provider_from_retailer is None:
                raise serializers.ValidationError(
                    'fff')

            print("Продукт успешно присвоен поставщику")

