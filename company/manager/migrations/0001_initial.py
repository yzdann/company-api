# Generated by Django 2.1.5 on 2019-02-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('street_line_1', models.CharField(max_length=255)),
                ('street_line_2', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
    ]
