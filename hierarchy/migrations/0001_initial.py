# Generated by Django 5.0.4 on 2024-05-01 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, verbose_name='почта')),
                ('country', models.CharField(max_length=50, verbose_name='страна')),
                ('city', models.CharField(max_length=50, verbose_name='город')),
                ('street', models.CharField(max_length=50, verbose_name='улица')),
                ('house_number', models.IntegerField(verbose_name='номер дома')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название продукта')),
                ('product_model', models.CharField(max_length=50, verbose_name='модель продукта')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='дата выхода продукта')),
            ],
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название завода')),
                ('provider', models.IntegerField(default=0, verbose_name='поставщик')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='задолженность')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hierarchy.contacts', verbose_name='контактные данные')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hierarchy.products', verbose_name='продукт')),
            ],
        ),
        migrations.CreateModel(
            name='Retail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название розничной сети')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='задолженность')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hierarchy.contacts', verbose_name='контактные данные')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hierarchy.products', verbose_name='продукт')),
                ('provider_from_factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hierarchy.factory', verbose_name='поставки с завода')),
            ],
        ),
        migrations.CreateModel(
            name='IndividualEntrepreneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название индивидуального предпринимателя')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='задолженность')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hierarchy.contacts', verbose_name='контактные данные')),
                ('provider_from_factory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hierarchy.factory', verbose_name='поставки с завода')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hierarchy.products', verbose_name='продукт')),
                ('provider_from_retailer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hierarchy.retail', verbose_name='поставки с розничной сети')),
            ],
        ),
    ]
