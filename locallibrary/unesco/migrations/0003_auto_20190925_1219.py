# Generated by Django 2.2.5 on 2019-09-25 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0002_auto_20190925_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='area_hectares',
            field=models.FloatField(blank=True, null=True),
        ),
    ]