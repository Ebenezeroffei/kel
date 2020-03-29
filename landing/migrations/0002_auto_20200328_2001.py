# Generated by Django 3.0.4 on 2020-03-28 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(upload_to='product_simages'),
        ),
    ]