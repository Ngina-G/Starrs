# Generated by Django 4.0.5 on 2022-06-15 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awwards', '0006_delete_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='', upload_to='profile/'),
        ),
    ]
