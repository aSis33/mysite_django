# Generated by Django 3.1.2 on 2020-10-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_Management_System', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmovie',
            name='Thumbnail',
            field=models.ImageField(upload_to='static'),
        ),
    ]