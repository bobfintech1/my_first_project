# Generated by Django 4.0.4 on 2022-04-24 23:18

import about.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('body', models.TextField()),
                ('data', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('image', models.ImageField(blank=True, null=True, upload_to=about.models.upload_location)),
            ],
        ),
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('body', models.TextField()),
                ('data', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('image', models.ImageField(blank=True, null=True, upload_to=about.models.upload_location)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
