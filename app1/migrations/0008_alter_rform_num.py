# Generated by Django 4.2.11 on 2024-03-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_rform_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rform',
            name='num',
            field=models.IntegerField(default='Null'),
        ),
    ]
