# Generated by Django 4.0.4 on 2022-06-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_index_num_of_dl_courses_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='welcome_header',
            new_name='welcome_header_blue',
        ),
        migrations.AddField(
            model_name='index',
            name='welcome_header_yellow',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]