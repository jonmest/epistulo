# Generated by Django 2.1.4 on 2019-01-08 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatorprofile',
            name='stripe_account_id',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]