# Generated by Django 2.0.2 on 2019-04-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190408_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='presentlivingplace',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
