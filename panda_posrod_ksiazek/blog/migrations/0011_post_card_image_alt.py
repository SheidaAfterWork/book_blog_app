# Generated by Django 3.0.2 on 2020-02-17 21:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0010_auto_20200217_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='card_image_alt',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
