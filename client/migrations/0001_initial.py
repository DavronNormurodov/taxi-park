# Generated by Django 4.0.2 on 2022-02-03 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('passport_series', models.CharField(max_length=9)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
    ]