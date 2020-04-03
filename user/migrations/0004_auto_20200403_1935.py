# Generated by Django 3.0.4 on 2020-04-03 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_auto_20200316_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='client',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
