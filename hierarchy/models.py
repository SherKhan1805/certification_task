from django.db import models

from config.utils import NULLABLE


class Contacts(models.Model):
    """
    Модель для хранения контактной информации.
    """
    email = models.CharField(
        max_length=200, verbose_name='почта')
    country = models.CharField(
        max_length=200, verbose_name='страна')
    city = models.CharField(
        max_length=200, verbose_name='город')
    street = models.CharField(
        max_length=200, verbose_name='улица')
    house_number = models.IntegerField(
        verbose_name='номер дома')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'контактные данные'
        verbose_name_plural = 'контактные данные'


class Products(models.Model):
    """
    Модель для хранения информации о продукте.
    """
    name = models.CharField(
        max_length=100, verbose_name='название продукта')
    product_model = models.CharField(
        max_length=100, verbose_name='модель продукта')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='дата выхода продукта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Factory(models.Model):
    """
    Модель для создания завода.
    Модель завода является поставщиком для всех других иерархий.
    """
    name = models.CharField(
        max_length=100, verbose_name='название завода')
    contacts = models.ForeignKey(
        Contacts, on_delete=models.CASCADE, verbose_name='контактные данные')
    products = models.ForeignKey(
        Products, on_delete=models.CASCADE, verbose_name='продукт')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'


class Retail(models.Model):
    """
    Модель для создания розничной сети.
    """
    name = models.CharField(
        max_length=100, verbose_name='название розничной сети')
    contacts = models.ForeignKey(
        Contacts, on_delete=models.CASCADE, verbose_name='контактные данные')
    products = models.ForeignKey(
        Products, on_delete=models.CASCADE, verbose_name='продукт')
    provider_from_factory = models.ForeignKey(
            Factory, on_delete=models.CASCADE, verbose_name='поставки с завода')
    debt = models.DecimalField(
        default=0.00, max_digits=10, decimal_places=2, verbose_name='задолженность')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'


class Entrepreneur(models.Model):
    """
    Модель для создания индивидуального предпринимателя.
    """
    name = models.CharField(
        max_length=100, verbose_name='название индивидуального предпринимателя')
    contacts = models.ForeignKey(
        Contacts, on_delete=models.CASCADE, verbose_name='контактные данные')
    products = models.ForeignKey(
        Products, on_delete=models.CASCADE, verbose_name='продукт')
    provider_from_factory = models.ForeignKey(
            Factory, on_delete=models.CASCADE, verbose_name='поставки с завода', **NULLABLE)
    provider_from_retailer = models.ForeignKey(
            Retail, on_delete=models.CASCADE, verbose_name='поставки с розничной сети', **NULLABLE)
    debt = models.DecimalField(
        default=0.00, max_digits=10, decimal_places=2, verbose_name='задолженность')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'индивидуальный предприниматель'
        verbose_name_plural = 'индивидуальные предприниматели'
