# Generated by Django 3.2.12 on 2023-06-14 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
    ]
