# Generated by Django 4.1.3 on 2023-03-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
    ]
