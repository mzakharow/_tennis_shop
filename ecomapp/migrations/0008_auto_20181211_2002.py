# Generated by Django 2.1.3 on 2018-12-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_auto_20181206_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='item',
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ManyToManyField(to='ecomapp.CartItem'),
        ),
    ]