# Generated by Django 5.0.4 on 2024-04-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0006_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='group',
            field=models.CharField(max_length=100),
        ),
    ]
