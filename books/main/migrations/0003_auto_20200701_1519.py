# Generated by Django 3.0.8 on 2020-07-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200701_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birthday',
            field=models.DateField(verbose_name='Date of birth'),
        ),
    ]
