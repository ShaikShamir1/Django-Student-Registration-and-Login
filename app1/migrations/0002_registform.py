# Generated by Django 4.2.11 on 2024-03-16 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.IntegerField()),
                ('num', models.IntegerField()),
                ('img', models.ImageField(upload_to='gallery')),
            ],
        ),
    ]
