# Generated by Django 5.0.4 on 2024-04-08 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0004_alter_pairing_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='groupname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='pairing',
        ),
    ]
