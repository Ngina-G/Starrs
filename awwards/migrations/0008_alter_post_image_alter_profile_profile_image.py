# Generated by Django 4.0.5 on 2022-06-15 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0007_alter_post_image_alter_post_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(upload_to='profile/'),
        ),
    ]
