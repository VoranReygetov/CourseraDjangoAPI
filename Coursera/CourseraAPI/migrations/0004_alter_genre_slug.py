# Generated by Django 4.2.5 on 2023-09-09 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseraAPI', '0003_genre_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
