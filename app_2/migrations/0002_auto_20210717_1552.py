from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='prices',
        ),
        migrations.AddField(
            model_name='company',
            name='prices',
            field=models.ManyToManyField(to='app_2.Prices'),
        ),
    ]
