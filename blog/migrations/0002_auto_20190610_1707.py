# Generated by Django 2.2.1 on 2019-06-10 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musician',
            old_name='instrument',
            new_name='Album',
        ),
    ]
