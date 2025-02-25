# Generated by Django 4.2.1 on 2024-08-07 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(default='default.jpg', upload_to='profile_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomAvatar',
        ),
    ]
