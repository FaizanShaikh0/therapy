# Generated by Django 4.1.6 on 2023-10-09 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='therepy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=25)),
                ('treatment', models.CharField(max_length=200)),
                ('fees', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('nextdate', models.DateField()),
            ],
        ),
    ]
