# Generated by Django 3.2.9 on 2021-12-09 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_genre_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_file',
            field=models.FileField(default=1, upload_to='books'),
            preserve_default=False,
        ),
    ]
