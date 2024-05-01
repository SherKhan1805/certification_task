# Generated by Django 5.0.4 on 2024-05-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IndividualEntrepreneur',
            new_name='Entrepreneur',
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'контактные данные', 'verbose_name_plural': 'контактные данные'},
        ),
        migrations.AlterModelOptions(
            name='entrepreneur',
            options={'verbose_name': 'индивидуальный предприниматель', 'verbose_name_plural': 'индивидуальные предприниматели'},
        ),
        migrations.AlterModelOptions(
            name='factory',
            options={'verbose_name': 'завод', 'verbose_name_plural': 'заводы'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterModelOptions(
            name='retail',
            options={'verbose_name': 'розничная сеть', 'verbose_name_plural': 'розничные сети'},
        ),
        migrations.AlterField(
            model_name='contacts',
            name='city',
            field=models.CharField(max_length=200, verbose_name='город'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='country',
            field=models.CharField(max_length=200, verbose_name='страна'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.CharField(max_length=200, verbose_name='почта'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='street',
            field=models.CharField(max_length=200, verbose_name='улица'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_model',
            field=models.CharField(max_length=100, verbose_name='модель продукта'),
        ),
    ]