# Generated by Django 3.0.2 on 2020-02-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_commited'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hero_image',
            field=models.ImageField(blank=True, upload_to='hero_images/% Y/% m/% d/'),
        ),
    ]
