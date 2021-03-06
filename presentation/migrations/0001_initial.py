# Generated by Django 4.0.4 on 2022-04-17 08:44

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
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presentation', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1024)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Презинтация',
                'verbose_name_plural': 'Презинтации',
            },
        ),
    ]
