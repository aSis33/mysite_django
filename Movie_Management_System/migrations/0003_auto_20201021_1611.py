# Generated by Django 3.1.2 on 2020-10-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_Management_System', '0002_auto_20201021_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmovie',
            name='Thumbnail',
            field=models.ImageField(upload_to='media/gallery'),
        ),
    ]
