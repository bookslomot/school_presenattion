# Generated by Django 4.0.4 on 2022-04-17 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='presentation',
            field=models.FileField(upload_to='presentation/%Y/%m/%d/'),
        ),
    ]
