# Generated by Django 3.0.2 on 2020-01-16 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_fhoto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='fhoto',
            new_name='photo',
        ),
    ]
