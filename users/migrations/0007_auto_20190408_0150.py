# Generated by Django 2.0.2 on 2019-04-07 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190408_0143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='presentlivingplace',
            new_name='presentlivingaddress',
        ),
    ]
