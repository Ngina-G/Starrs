# Generated by Django 4.0.5 on 2022-06-14 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0003_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_photo',
            new_name='profile_image',
        ),
    ]