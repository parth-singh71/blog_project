# Generated by Django 3.0.5 on 2020-04-22 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sate_posted',
            new_name='date_posted',
        ),
    ]
