# Generated by Django 5.1.3 on 2024-12-05 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Book',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='Cart',
            new_name='cart',
        ),
    ]