# Generated by Django 3.2.5 on 2021-07-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_2', '0004_alter_company_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='closing_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prices',
            name='highest_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prices',
            name='lowest_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prices',
            name='opening_price',
            field=models.FloatField(),
        ),
    ]