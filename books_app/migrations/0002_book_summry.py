# Generated by Django 5.0.7 on 2024-07-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='summry',
            field=models.TextField(default='test uchun'),
            preserve_default=False,
        ),
    ]
