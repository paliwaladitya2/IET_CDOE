# Generated by Django 4.0.4 on 2022-06-24 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_index_useful_link_useful_links_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_details',
            name='course_eligibility',
            field=models.TextField(default='Lorem ipsum gravida nibh vel velit auctor aliquetn sollicitudirem quibibendum auci elit cons equat ipsutis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris. Morbi accumsan ipsum velit. Nam nec tellus .', max_length=400),
        ),
    ]
