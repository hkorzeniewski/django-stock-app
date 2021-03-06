# Generated by Django 3.2.5 on 2021-07-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_price', models.DecimalField(decimal_places=2, max_digits=2)),
                ('highest_price', models.DecimalField(decimal_places=2, max_digits=2)),
                ('lowest_price', models.DecimalField(decimal_places=2, max_digits=2)),
                ('closing_price', models.DecimalField(decimal_places=2, max_digits=2)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(choices=[('ACP', 'ASSECO'), ('ALE', 'ALLEGRO'), ('CCC', 'CCC')], max_length=10)),
                ('prices', models.ManyToManyField(to='app_2.Prices')),
            ],
        ),
    ]
