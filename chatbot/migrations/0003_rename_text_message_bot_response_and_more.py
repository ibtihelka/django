# Generated by Django 5.1.2 on 2024-10-28 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_rename_bot_response_message_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='text',
            new_name='bot_response',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AddField(
            model_name='message',
            name='user_message',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
