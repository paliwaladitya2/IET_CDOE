# Generated by Django 4.0.4 on 2022-05-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_index_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to='slides/'),
        ),
    ]