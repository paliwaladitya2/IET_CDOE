# Generated by Django 4.0.4 on 2022-06-26 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_announcements_index_announcements_on_load'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='website',
            field=models.URLField(default='#'),
        ),
    ]