# Generated by Django 4.2.6 on 2023-10-23 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makenote_app', '0004_alter_note_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
    ]