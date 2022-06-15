# Generated by Django 4.0.5 on 2022-06-15 00:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awwards', '0004_rename_profile_photo_profile_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='clone/')),
                ('name', models.CharField(max_length=50)),
                ('image_caption', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='like_image', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post', to='awwards.profile')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
