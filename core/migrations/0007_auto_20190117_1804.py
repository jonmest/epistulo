# Generated by Django 2.1.5 on 2019-01-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_creatorprofile_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatorprofile',
            name='cover_pic',
            field=models.ImageField(blank=True, null=True, upload_to='img_folder/'),
        ),
    ]