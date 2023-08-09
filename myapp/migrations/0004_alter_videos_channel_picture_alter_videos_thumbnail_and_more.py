# Generated by Django 4.2.3 on 2023-08-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_userprofile_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='channel_picture',
            field=models.ImageField(upload_to='channel-pictures/'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='thumbnail',
            field=models.ImageField(upload_to='thumbnails/'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video_time',
            field=models.CharField(max_length=50),
        ),
    ]