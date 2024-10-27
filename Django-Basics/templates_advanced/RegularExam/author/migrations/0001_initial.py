# Generated by Django 5.1.2 on 2024-10-27 09:30

import author.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, validators=[author.models.validate_letters_only])),
                ('last_name', models.CharField(max_length=50, validators=[author.models.validate_letters_only])),
                ('passcode', models.CharField(max_length=6)),
                ('pets_number', models.PositiveSmallIntegerField()),
                ('info', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
