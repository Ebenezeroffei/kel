# Generated by Django 3.0.4 on 2020-04-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_usercartitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercartitems',
            name='item_quantity',
            field=models.IntegerField(default=1),
        ),
    ]
