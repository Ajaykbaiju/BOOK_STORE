# Generated by Django 5.1.3 on 2024-11-30 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_author2_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1, upload_to='book_media'),
            preserve_default=False,
        ),
    ]
