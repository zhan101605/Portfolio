# Generated by Django 4.2.17 on 2024-12-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('cpNumber', models.CharField(max_length=100)),
            ],
        ),
    ]