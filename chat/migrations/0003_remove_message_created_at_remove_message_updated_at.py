# Generated by Django 5.1.2 on 2024-10-26 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_created_at_message_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='message',
            name='updated_at',
        ),
    ]
